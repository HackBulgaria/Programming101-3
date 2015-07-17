from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship


Base = declarative_base()

class Student(Base):
    __tablename__ = "Students"
    student_id = Column(Integer, primary_key=True)
    student_fn = Column(String(20), unique=True)
    student_name = Column(String)

class Grade(Base):
    __tablename__ = "Grades"
    grade_id = Column(Integer, primary_key=True)
    grade_value = Column(Integer)
    student_id = Column(Integer, ForeignKey("Students.student_id"))
    student = relationship(Student, backref="grades")

engine = create_engine("sqlite:///classroom.sqlite3")

Base.metadata.create_all(engine)

session = Session(bind=engine)

