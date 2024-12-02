from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session


from models import Base, Author, Genre, Book

engine = create_engine("sqlite:///ORM/books.db")
    
Base.metadata.create_all(bind=engine)

# простой вывод 
def get_all_books():   
    with Session(autoflush=False, bind=engine) as db:
        authors = db.query(Author).all()
        print(authors)
        print('-'*20)
        genres = db.query(Genre).all()
        print(genres)
        books = db.query(Book).all()
        print(books)

    


# агрегирующие функции
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
        


def get_join_tables():
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Book, Genre, Author)
        # print (*query, end='\n')
        for book, genre, author in query:
            print(book, '|', genre, '|', author)
    


     
get_aggregate()
get_join_tables()