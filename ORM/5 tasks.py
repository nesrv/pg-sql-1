## Задача 1

# Для книг, которые уже есть на складе (в таблице `book`) по той же цене, 
# что и в поставке (`supply`), увеличить количество на значение, указанное в поставке, 
# а также обнулить количество этих книг в поставке.


from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

from models import Book, Supply, Base

engine = create_engine("sqlite:///ORM/books.db", echo=True)
# Base.metadata.create_all(bind=engine)
    
def get_book_join_supply():
    with Session(autoflush=False, bind=engine) as db:
        query = db.query(Book, Supply).filter(Book.price == Supply.price).all()
        test1 = db.query(Book).filter(Book.title=="Мастер и Маргарита").first()
        test1.amount += 1
        db.commit()
        print(test1)
        
        
        
        for book, supply in query:
            # current_book = db.query(Book).filter(Book.book_id == book.book_id).first()
            # print(current_book)
            # current_book.amount += supply.amount
            print(book.title, book.amount,supply.amount) 
            # book.amount += supply.amount
            # print(book.title, book.amount,supply.amount) 
            # current_book.amount +=supply.amount
            # book.Supply.amount = 0
            
        # db.commit()
        
     
get_book_join_supply()
