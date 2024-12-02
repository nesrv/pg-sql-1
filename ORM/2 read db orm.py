from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Session




engine = create_engine("sqlite:///ORM/books.db")

class Base(DeclarativeBase): pass

class Author(Base):
    __tablename__ = "author"
  
    author_id = Column(Integer, primary_key=True, index=True)
    name_author = Column(Text)
    
    def __repr__(self):
        return f"Author(author_id={self.author_id}, name_author={self.name_author})"

class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(Integer, primary_key=True, index=True)
    name_genre = Column(Text)

    def __repr__(self):
        return f"Genre(genre_id={self.genre_id}, name_genre={self.name_genre})"   
    
class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    author_id = Column(Integer)
    genre_id = Column(Integer)
    price = Column(Numeric(10,2))
    amount = Column(Integer)
    author_id = Column(Integer, ForeignKey("author.id"))
    genre_id = Column(Integer, ForeignKey("genre.id"))

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title={self.title}, author_id={self.author_id}, genre_id={self.genre_id}, price={self.price}, amount={self.amount})"    
    
        
    
Base.metadata.create_all(bind=engine)

with Session(autoflush=False, bind=engine) as db:
    authors = db.query(Author).all()
    print(authors)
    print('-'*20)
    genres = db.query(Genre).all()
    print(genres)
    books = db.query(Book).all()
    print(books)

