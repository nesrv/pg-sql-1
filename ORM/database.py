from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine


engine = create_engine("sqlite:///ORM/books.db")

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass