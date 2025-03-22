from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    PrimaryKeyConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    student_id = Column(Integer, primary_key=True)
    name_student = Column(String)
   
    def __repr__(self):
        return f"{self.name_student}"    

class Attempt(Base):
    __tablename__ = "attempt"

    attempt_id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    subject_id = Column(Integer)
    date_attempt = Column(Date)
    result = Column(Integer)


class Subject(Base):
    __tablename__ = 'subject'
    
    subject_id = Column(Integer, primary_key=True)
    name_subject = Column(String)


class Question(Base):
    __tablename__ = 'question'
    
    question_id = Column(Integer, primary_key=True)
    name_question = Column(String)
    subject_id = Column(Integer)
    

class Answer(Base):
    __tablename__ = 'answer'
    
    answer_id = Column(Integer, primary_key=True)
    name_answer = Column(String)
    question_id = Column(Integer)
    is_correct = Column(Integer) 

class Testing(Base):
    __tablename__ = 'testing'
    
    testing_id = Column(Integer, primary_key=True)
    attempt_id = Column(Integer)
    question_id = Column(Integer)
    answer_id = Column(Integer)