# Задача 1

# Для книг, которые уже есть на складе (в таблице `book`) по той же цене,
# что и в поставке (`supply`), увеличить количество на значение, указанное в поставке,
# а также обнулить количество этих книг в поставке.


from database import session_factory
from models import Author, Genre, Book, Supply
from sqlalchemy import Integer, cast, func, select


def update_amount_from_supply():
    with session_factory() as db:
        query = db.query(Book, Supply).filter(Book.price == Supply.price).all()
        for b, s in query:
            b.amount += s.amount
            s.amount = 0
        db.commit()


# update_amount_from_supply()


# Задача 2. Добавить новые записи о книгах, которые есть в таблице `supply` и нет в таблице `book`.
# Поскольку в таблице `supply` не указан жанр книги, оставить его пока пустым (занести значение `Null`).


def add_new_authors():
    with session_factory() as db:
        query = db.query(Supply).all()

        for supply in query:
            author = db.query(Author).filter(
                Author.name_author == supply.author).first()
            if author is None:
                author = Author(name_author=supply.author)
                db.add(author)

        db.commit()

# add_new_authors()

# Задача 3. Добавить новые записи о книгах, которые есть в таблице `supply` и нет в таблице `book`.
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
                    author_id=db.query(Author).filter(
                        Author.name_author == supply.author).first().author_id,
                    price=supply.price,
                    amount=0
                )
                db.add(book)
                db.commit()


# add_new_books()


# Задача 4. Удалить всех авторов и все их книги, количество книг которых меньше 10.

def del_books_and_authors():
    with session_factory() as db:
        books = db.query(Book).all()
        for book in books:
            if book.amount < 10:
                author = db.query(Author).filter(
                    Author.author_id == book.author_id).first()
                if author:
                    db.delete(author)
                db.delete(book)

        db.commit()


# del_books_and_authors()

# Задача 5. Сгруппировать авторов по количество книг.

def del_books_and_authors_by_total_amount():
    with session_factory() as db:
        books = db.query(Book).count()
        print(books)
        # amount_authors= db.query(func.sum(Book.author_id)).scalar()
        amount_book_by_authors = db.query(Book.author_id, func.count(
            Book.amount)).group_by(Book.author_id).all()
        print(*amount_book_by_authors)

# del_books_and_authors_by_total_amount()

# Задача 6. Вывести товарную стоимость  книг по авторам


def get_total_price():
    with session_factory() as db:
        total_price = db.query(Book.author_id, func.sum(
            Book.price * Book.amount)).group_by(Book.author_id).all()
        total_price_by_authors = db.query(Book.author_id, Author.name_author,
                                          func.count(Book.amount),
                                          func.avg(Book.price),
                                          func.round(func.sum(Book.price * Book.amount) / func.count(Book.amount), 2)) \
            .join(Book).group_by(Author.name_author)\
            .order_by(func.count(Book.amount)).all()
        print(*total_price_by_authors)


get_total_price()

def get_total_price_2():
    with session_factory() as db:
        query = (
            select(
                Book.author_id,
                cast(func.avg(Book.price), Integer).label("Средняя цена"),
            )
            .group_by(Book.author_id)
        )
       
        # print(query.compile(compile_kwargs={"literal_binds": True}))
        result = db.execute(query).all()
        print(result)

get_total_price_2()


def test_without_group_by():
    with session_factory() as db:
        authors = db.query(Book.author).all()
        print(authors)

# test_without_group_by()
