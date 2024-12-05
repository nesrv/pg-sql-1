from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import create_engine
import psycopg2

# engine = create_engine("sqlite:///ORM/books.db") # for sqlite

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/books") # for postgresql


session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass