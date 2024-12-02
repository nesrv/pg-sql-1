from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from models import Author, Genre, Book

engine = create_engine("sqlite:///ORM/books.db")


def get_aggregate():
    with Session(autoflush=False, bind=engine) as db:
        count = db.query(func.count(Book.book_id)).scalar()
        print('Count books:', count)
        max_price = db.query(func.max(Book.price)).scalar()
        print('Maximum product price:', max_price)
        min_price = db.query(func.min(Book.price)).scalar()
        print('Minimum product price:', min_price)
        sum_price = db.query(func.sum(Book.price * Book.amount)).scalar()
        print('Sum price:', sum_price)
        min_book = db.query(Book).filter(Book.price == min_price).first()
        max_book = db.query(Book).filter(Book.price == max_price).first()
        print(min_book)
        print(max_book)
        

     
get_aggregate()
