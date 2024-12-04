## Задача 1

# Для книг, которые уже есть на складе (в таблице `book`) по той же цене, 
# что и в поставке (`supply`), увеличить количество на значение, указанное в поставке, 
# а также обнулить количество этих книг в поставке.


from database import session_factory
from models import Author, Genre, Book, Supply
    
def update_amount_from_supply():
    with session_factory() as db:
        query = db.query(Book, Supply).filter(Book.price == Supply.price).all()
        for b,s in query:
            b.amount += s.amount
            s.amount = 0       
        db.commit()
        
get_book_join_supply        
        
        
## Задача 2. Добавить новые записи о книгах, которые есть в таблице `supply` и нет в таблице `book`. 
# Для таких книг установить количество в 0, а для остальных - в соответствии с поставкой.
# Не забудьте учесть, что в таблице `supply` не указан жанр книги, оставить его пока пустым (занести значение `Null`).
# Прежде всего необходимо сформировать запрос с полями, которые соответствуют полям таблицы book,
# так как использовать только таблицу supply нельзя - в ней вместо кода автора стоит его фамилия.

def add_new_book():
    with session_factory() as db:
        query = db.query(Supply).all()
        for supply in query:
            book = db.query(Book).filter(Book.title == supply.title, Book.author_id == supply.author_id).first()
            if book is None:
                book = Book(title=supply.title, author_id=supply.author_id, price=supply.price, amount=0)
                db.add(book)
            else:
                book.amount += s.amount
                supply.amount = 0
        db.commit()
        

