## Задача 1

# Для книг, которые уже есть на складе (в таблице `book`) по той же цене,
# что и в поставке (`supply`), увеличить количество на значение, указанное в поставке,
# а также обнулить количество этих книг в поставке.


from database import session_factory
from models import Author, Genre, Book, Supply


def update_amount_from_supply():
    with session_factory() as db:
        query = db.query(Book, Supply).filter(Book.price == Supply.price).all()
        for b, s in query:
            b.amount += s.amount
            s.amount = 0
        db.commit()


# update_amount_from_supply()


## Задача 2. Добавить новые записи о книгах, которые есть в таблице `supply` и нет в таблице `book`. 
# Поскольку в таблице `supply` не указан жанр книги, оставить его пока пустым (занести значение `Null`).


def add_new_authors():
    with session_factory() as db:
        query = db.query(Supply).all()

        for supply in query:
            author = db.query(Author).filter(Author.name_author == supply.author).first()
            if author is None:
                author = Author(name_author=supply.author)
                db.add(author)
            
        db.commit()

# add_new_authors()

## Задача 3. Добавить новые записи о книгах, которые есть в таблице `supply` и нет в таблице `book`.
# Для таких книг установить количество в 0, а для остальных - в соответствии с поставкой.
# Не забудьте учесть, что в таблице `supply` не указан жанр книги, оставить его пока пустым (занести значение `Null`).


def add_new_books():
    with session_factory() as db:
        supplies = db.query(Supply).all()
        # authors = db.query(Author).all()
        
        for supply in supplies:
            book = db.query(Book).filter(Book.title == supply.title).first()
            
        if book is None:
            book = Book(
                title=supply.title,
                author_id=db.query(Author).filter(Author.name_author == supply.author).first().author_id,                    
                price=supply.price,
                amount=0
            )
            db.add(book)                
            db.commit()


add_new_books()
