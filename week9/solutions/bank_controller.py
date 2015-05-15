from models import Client
from base import Base

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class BankController:
    
    def __init__(self, db_connection_string):
        self.__engine = create_engine(db_connection_string)
        self.__session = Session(bind=self.__engine)
        
        Base.metadata.create_all(self.__engine)
