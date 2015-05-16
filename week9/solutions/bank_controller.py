import datetime
from models import Client, LoginAttempt
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from authentication_controller import AuthenticatonController
from transaction_controller import TransactionController

from helpers import hash_password


class BankController:
    
    def __init__(self, db_connection_string, block_after_n_logins = 5, block_for_n_minutes = 5):
        self.__engine = create_engine(db_connection_string)
        Base.metadata.create_all(self.__engine)

        self.__session = Session(bind=self.__engine)
        self.__auth = AuthenticatonController(self.__session, block_after_n_logins=block_after_n_logins, block_for_n_minutes=block_for_n_minutes)
        self.__transactions = TransactionController(self.__session) 
    
    def __commit_changes(self, objects):
        self.__session.add_all(objects)
        self.__session.commit()

    def register(self, username, password):
        return self.__auth.register(username, password)

    def login(self, username, password):
        return self.__auth.login(username, password)
    
    def create_account(self, user, account_name):
        return self.__transactions.create_account(user, account_name)

