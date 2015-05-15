from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey

from base import Base

class Client(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

