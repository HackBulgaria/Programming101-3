import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from base import Base

class Client(Base):
    __tablename__ = "Clients"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)

class LoginAttempt(Base):
    __tablename__ = "Login_Attempts"
    id = Column(Integer, primary_key=True)
    attempt_status = Column(String) # "Success", "Failure"
    attempt_timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Integer, ForeignKey(Client.id))
    user = relationship(Client, backref="login_attempts")
