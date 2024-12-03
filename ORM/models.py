from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey, func
from sqlalchemy.orm import DeclarativeBase, Session, relationship, mapped_column

class Base(DeclarativeBase): pass

class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(Integer, primary_key=True, index=True)
    name_genre = Column(Text)
    book = relationship(back_populates="genre", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Genre(genre_id={self.genre_id}, name_genre={self.name_genre})"  


class Author(Base):
    __tablename__ = "author"
  
    author_id = Column(Integer, primary_key=True, index=True)
    name_author = Column(Text)    
    book = relationship(back_populates="author", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"Author(author_id={self.author_id}, name_author={self.name_author})"

 
    
class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    author_id = Column(Integer)
    genre_id = Column(Integer)
    price = Column(Numeric(10,2))
    amount = Column(Integer)
    # author_id = relationship("Author", backref="book")
    # genre_id = relationship("Genre", backref="book")
    author_id = mapped_column(ForeignKey("author.id"))
    author = relationship('Author',back_populates = "author")
    genre_id = mapped_column(ForeignKey("genre.id"))
    genre = relationship('Genre', back_populates = "genre")
    
    # author_id = Column(Integer, ForeignKey("author.id"))
    # genre_id = Column(Integer, ForeignKey("genre.id"))

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title={self.title}, author_id={self.author_id}, genre_id={self.genre_id}, price={self.price}, amount={self.amount})"    
    
class Supply(Base):
    __tablename__ = "supply"

    supply_id = Column(Integer, primary_key=True, index=True)
    title = Column(Text)
    author = Column(Integer)
    price = Column(Numeric(10, 2))
    amount = Column(Integer)

    def __repr__(self):
        return f"Supply(supply_id={self.supply_id}, title={self.title}, author={self.author}, price={self.price}, amount={self.amount})"
    