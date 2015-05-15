from models import Client
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
        return self.__session.query(Client).filter(Client.username == username).count() == 1

    def register(self, username, password):
        if self.__is_registered(username):
            return False
        
        client = Client(username=username, password=hash_password(password))

        self.__session.add(client)
        self.__session.commit()
        
        return True
