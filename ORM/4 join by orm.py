from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from models import Author, Genre, Book

engine = create_engine("sqlite:///ORM/books.db")
    
def get_join_tables():
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Book, Genre, Author)
        # print (*query, end='\n')
        for book, genre, author in query:
            print(book, '|', genre, '|', author)
    
     
get_join_tables()