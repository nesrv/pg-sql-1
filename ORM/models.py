from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from database import Base


class Worker(Base):
    __tablename__ = "worker"

    worker_id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]

class Genre(Base):
    __tablename__ = "genre"

    genre_id: Mapped[int] = mapped_column(primary_key=True)
    name_genre: Mapped[str] 
    book = relationship('Book', back_populates="genre", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Genre(genre_id={self.genre_id}, name_genre={self.name_genre})"


# parent class
class Author(Base):
    __tablename__ = "author"
    author_id: Mapped[int] = mapped_column(primary_key=True)
    name_author: Mapped[str]

    book = relationship('Book', back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Author(author_id={self.author_id}, name_author={self.name_author})"


# child class
class Book(Base):
    __tablename__ = "book"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("author.author_id"))
    genre_id: Mapped[int] = mapped_column(ForeignKey("genre.genre_id", ondelete='SET NULL'), default=None)
    price: Mapped[float]
    amount: Mapped[int]
    author: Mapped["Author"] = relationship(back_populates="book")
    genre: Mapped["Genre"] = relationship(back_populates="book")

    def __repr__(self):
        return f"Book(book_id={self.book_id}, title={self.title}, author_id={self.author_id}, genre_id={self.genre_id}, price={self.price}, amount={self.amount})"


class Supply(Base):
    __tablename__ = "supply"

    supply_id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    price: Mapped[float]
    amount: Mapped[int]

    def __repr__(self):
        return f"Supply(supply_id={self.supply_id}, title={self.title}, author={self.author}, price={self.price}, amount={self.amount})"
