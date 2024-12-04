from database import session_factory
from models import Author, Genre, Book


#cross join
def get_join_tables():
    with session_factory() as db:
        query = db.query(Book, Genre, Author)
        # print (*query, end='\n')
        for book, genre, author in query:
            print(book, '|', genre, '|', author)

# get_join_tables()    

#inner join
def get_join_tables():
    with session_factory() as db:
        query = db.query(Book, Genre, Author).join(Genre).join(Author)
        # print (*query, end='\n')
        for book, genre, author in query:
            print(book, '|', genre, '|', author)

# get_join_tables()


#left outer join
def get_join_tables():
    with session_factory() as db:
        query = db.query(Book, Genre, Author).outerjoin(Genre).outerjoin(Author)
        # print (*query, end='\n')
        for book, genre, author in query:
            print(book, '|', genre, '|', author)


get_join_tables()