from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeBase, Session


sqlite_database = "books.db"

# engine = create_engine(sqlite_database, echo=True)

# class Base(DeclarativeBase): pass
# class Author(Base):
#     __tablename__ = "author"
  
#     author_id = Column(Integer, primary_key=True, index=True)
#     name_author = Column(Text)
    
# Base.metadata.create_all(bind=engine)

# with Session(autoflush=False, bind=engine) as db:
#     authors = db.query(Author).all()
#     # for author in authors:
#     #     print(author.author_id, author.name_author)
#     print(authors)

import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sqlite_database = os.path.join(BASE_DIR, "books.db")


con = sqlite3.connect(sqlite_database)
cursor = con.cursor()
cursor.execute("SELECT * FROM author")

print(cursor.fetchall())