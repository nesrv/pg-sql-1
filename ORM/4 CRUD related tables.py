from database import session_factory
from models import Worker, Book



def insert_book():
    with session_factory() as s:
        book = Book(title="Book 5", author_id=1, genre_id=1, price=100, amount=10)
        # book = Book(title="Book 4", author_id=3)
        s.add(book)
        s.commit()

insert_book()



def update_book():
    with session_factory() as s:
        # book = s.query(Book).filter_by(title="Book 1").first()
        # book = s.query(Book).filter_by(title="Book 2").first()
        book = s.query(Book).filter_by(title="Updated book 3").first()
        book.title = 'Updated Updated book 3' 
        # book.author_id = 2 
        # book.genre_id = 2
        s.commit()

update_book()


