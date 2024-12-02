## Задача 1

# Для книг, которые уже есть на складе (в таблице `book`) по той же цене, 
# что и в поставке (`supply`), увеличить количество на значение, указанное в поставке, 
# а также обнулить количество этих книг в поставке.


from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from models import Book, Supply

engine = create_engine("sqlite:///ORM/books.db")
    
def get_book_join_supply():
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Book, Supply).filter(Book.price == Supply.price).all()
        # print(query)
        for book in query:
            print(book.Book.title, book.Supply.price) 
    
     
get_book_join_supply()