import datetime
from models import Client, LoginAttempt
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from helpers import hash_password


class BankController:
    
    def __init__(self, db_connection_string, block_after_n_logins = 5, block_for_n_minutes = 5):
        self.__engine = create_engine(db_connection_string)
        self.__session = Session(bind=self.__engine)
        
        self.__settings = {
            "block_after_n_logins": block_after_n_logins,
            "block_for_n_minutes": block_for_n_minutes
        }
        
        Base.metadata.create_all(self.__engine)
    
    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()
    
    def __is_registered(self, username):
        try:
            user = self.__session.query(Client).filter(Client.username == username).one()
            return user
        except:
            return None
    
    def __success_login_attempt(self, user):
        user.login_attempts.append(LoginAttempt(attempt_status=LoginAttempt.SUCCESSFUL_ATTEMPT))
        self.__commit_changes([user])
    
    def __failed_login_attempt(self, user):
        user.login_attempts.append(LoginAttempt(attempt_status=LoginAttempt.FAILED_ATTEMPT))
        self.__commit_changes([user])

    def __block_user(self, user):
        user.is_blocked = True
        delta = datetime.timedelta(minutes=self.__settings["block_for_n_minutes"])
        user.blocked_until = datetime.datetime.utcnow() + delta 
        self.__commit_changes([user])
    
    def __unblock_user(self, user):
        user.is_blocked = False
        user.blocked_until = None
        
        # Break the last 5 failed attempts
        user.login_attempts.append(LoginAttempt(attempt_status = LoginAttempt.AFTER_BLOCK, user_id = user.id))
        self.__commit_changes([user])
    
    def __can_login_after_block(self, user):
        now = datetime.datetime.utcnow()
        print(now)
        print(user.blocked_until)
        return now >= user.blocked_until

    def __can_login(self, user):
        if user.is_blocked:
            if self.__can_login_after_block(user):
                self.__unblock_user(user)
                return True
            return False

        block_after_n_logins = self.__settings["block_after_n_logins"]

        login_attemps = self.__session.query(LoginAttempt).filter(LoginAttempt.user_id == user.id).all()
        last_n_failed = [a.attempt_status == LoginAttempt.FAILED_ATTEMPT for a in login_attemps[-block_after_n_logins:]]
        
        if len(last_n_failed) < block_after_n_logins:
            return True

        if all(last_n_failed):
            self.__block_user(user)
            return False
        
        return True

    def register(self, username, password):
        if self.__is_registered(username) is not None:
            return False
        
        client = Client(username=username, 
                        password=hash_password(password), 
                        is_blocked=False,
                        blocked_until = None)

        self.__commit_changes([client])
        
        return True
    
    def login(self, username, password):
        user = self.__is_registered(username)

        if user is None:
            return "USER_NOT_EXISTS"

        if not self.__can_login(user):
            return "USER_BLOCKED"
    
        password = hash_password(password)

        if user.password == password:
            self.__success_login_attempt(user)
            return user
        
        self.__failed_login_attempt(user)
        return "FAILED_LOGIN"

