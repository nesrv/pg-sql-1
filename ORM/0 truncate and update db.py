from database import engine, session_factory, Base
from models import *


autors = [
    "Булгаков М.А.",
    "Достоевский Ф.М.",
    "Есенин С.А.",
    "Пастернак Б.Л.",
    "Лермонтов М.Ю.",
]

books = [
    ("Мастер и Маргарита", 1, 1, 670.99, 3),
    ("Белая гвардия", 1, 1, 540.50, 5),
    ("Идиот", 2, 1, 460.00, 10),
    ("Братья Карамазовы", 2, 1, 799.01, 3),
    ("Игрок", 2, 1, 480.50, 10),
    ("Стихотворения и поэмы", 3, 2, 650.00, 15),
    ("Черный человек", 3, 2, 570.20, 6),
    ("Лирика", 4, 2, 518.99, 2),
]


supplies = [
    ("Доктор Живаго", "Пастернак Б.Л.", 380.80, 4),
    ("Черный человек", "Есенин С.А.", 570.20, 6),
    ("Белая гвардия", "Булгаков М.А.", 540.50, 7),
    ("Идиот", "Достоевский Ф.М.", 360.80, 3),
    ("Стихотворения и поэмы", "Лермонтов М.Ю.", 255.90, 4),
    ("Остров сокровищ", "Стивенсон Р.Л.", 599.99, 5),
]

genres = [
    "Роман",
    "Поэзия",
    "Приключения",
]


def create_db():
    with session_factory() as db:
        Author.metadata.create_all(engine)
        Genre.metadata.create_all(engine)
        Book.metadata.create_all(engine)
        Supply.metadata.create_all(engine)

        db.commit()


def truncate_db():
    with session_factory() as db:
        # User.__table__.drop(engine)
        Base.metadata.drop_all(
            engine,
            tables=[
                Supply.__table__,
                Genre.__table__,
                Author.__table__,
                Book.__table__,
            ],
        )
        Base.metadata.create_all(
            engine,
            tables=[
                Supply.__table__,
                Genre.__table__,
                Author.__table__,
                Book.__table__,
            ],
        )

   
def fill_db():
    with session_factory() as db:
        for author in autors:
            db.add(Author(name_author=author))
        for genre in genres:
            db.add(Genre(name_genre=genre))
        for book in books:
            db.add(
                Book(
                    title=book[0],
                    author_id=book[1],
                    genre_id=book[2],
                    price=book[3],
                    amount=book[4],
                )
            )
        for supply in supplies:
            db.add(
                Supply(
                    title=supply[0],
                    author=supply[1],
                    price=supply[2],
                    amount=supply[3],
                )
            )
        db.commit()

create_db()
truncate_db()
fill_db()

