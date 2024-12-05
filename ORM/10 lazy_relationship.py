from database import session_factory
from models import Author, Genre, Book, Supply
from sqlalchemy import Integer, cast, func, select
from sqlalchemy.orm import joinedload, selectinload


def select_books_with_lazy_relation():
    with session_factory() as db:
        query = select(Book)
        res = db.execute(query)
        result = res.scalars().all()
        book_1_author = result[0].author
        print(book_1_author.name_author)

        book_1_genre = result[0].genre
        print(book_1_genre.name_genre)


def select_books_with_joined_relation():
    with session_factory() as db:
        query = select(Book).options(joinedload(Book.author))

        res = db.execute(query)
        # result = res.scalars().all()
        result = res.unique().scalars().all()
        book_1_author = result[0].author
        print(book_1_author.name_author)

        book_1_genre = result[0].genre
        print(book_1_genre.name_genre)


select_books_with_joined_relation()

# select_books_with_lazy_relation()
