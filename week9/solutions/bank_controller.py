from models import Client, LoginAttempt
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from helpers import hash_password


class BankController:
    
    def __init__(self, db_connection_string):
        self.__engine = create_engine(db_connection_string)
        self.__session = Session(bind=self.__engine)
        
        Base.metadata.create_all(self.__engine)
     
    def __is_registered(self, username):
        try:
            user = self.__session.query(Client).filter(Client.username == username).one()
            return user
        except:
            return None
    
    def __success_login_attempt(self, user):
        user.login_attempts.append(LoginAttempt(attempt_status="success"))

        self.__session.add(user)
        self.__session.commit()
    
    def __failed_login_attempt(self, username):
        user = self.__is_registered(username)

        if user is None:
            return

        user.login_attempts.append(LoginAttempt(attempt_status="failed"))

        self.__session.add(user)

    def register(self, username, password):
        if self.__is_registered(username) is not None:
            return False
        
        client = Client(username=username, password=hash_password(password))

        self.__session.add(client)
        
        return True
    
    def login(self, username, password):
        password = hash_password(password)
        try:
            user = self.__session.query(Client) \
                .filter(Client.username == username, Client.password == password) \
                .one()
            self.__success_login_attempt(user)
            return user
        except:
            self.__failed_login_attempt(username)
            return None
        finally:
            self.__session.commit()
