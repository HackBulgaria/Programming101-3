from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()

class Person(Base):
    __tablename__ = "People"
    person_id = Column(Integer, primary_key=True)
    person_name = Column(String)
    person_gender = Column(String)
    
    def __str__(self):
        return self.person_name

engine = create_engine("sqlite:///people_db")
Base.metadata.create_all(engine)

session = Session(bind=engine)

gosho = Person(person_name="Gosho", person_gender="male")
print(gosho)

session.add(gosho)
session.commit()










