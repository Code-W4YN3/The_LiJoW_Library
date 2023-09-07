from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine, insert, delete
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy
import random

Base = declarative_base()
engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    author = Column(String())
    genre = Column(String())
    reader_count = Column(Integer())

    reviews = relationship('Review', back_populates='book')
    readers = association_proxy('reviews', 'reader',
        creator=lambda rd: Review(reader=rd))

    def __repr__(self):
        return f"Book {self.id}: " \
            + f"Name: {self.name}, " \
            + f"Author: {self.author}"\
            + f"Genre: {self.genre}" \
            + f"Readers: {self.reader_count}"

    def book_name(self):
        return self.name

    def book_author(self):
        return self.author

    def book_genre(self):
        return self.genre

    def total_reader_count(self):
        return self.reader_count

    def all_reviews(self):
        return [review.rating for review in self.reviews]

    def all_readers(self):
        return [reader.get_full_name() for reader in self.readers]

    def most_popular_book(self):
        for review in self.reviews:
            if review.rating == max(review.rating for review in self.reviews):
                return review.book.name

    @classmethod
    def all_books(cls):
        books = session.query(Book).all()
        for i in books:
            print(f"{i.id}.{i.name} by {i.author}, {i.genre}")
        return " "

    @classmethod
    def add_book(cls,name, author, genre):
        new_row = Book(name=f"{name}", author=f"{author}", genre=f"{genre}", reader_count=random.randint(1, 100))
        session.add(new_row)
        session.commit()

    @classmethod
    def remove_book(cls, bk_id):
        rm_book = session.query(Book).filter(Book.id == bk_id).first()
        session.delete(rm_book)
        session.commit()


class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    library_id = Column(Integer())

    reviews = relationship('Review', back_populates='reader')
    books = association_proxy('reviews', 'book',
        creator=lambda bk: Review(book=bk))

    def __repr__(self):
        return f"Reader {self.id}: " \
            + f"First_name: {self.first_name}" \
            + f"Last_name: {self.last_name}" \
            + f"Library_id: {self.library_id}"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_library_id(self):
        return self.library_id

    def favorite_book(self):
        for review in self.reviews:
            if review.rating == max(review.rating for review in self.reviews):
                return review.book.name

    @classmethod
    def all_readers(cls):
        readers = session.query(Reader).all()
        for i in readers:
            print(f"{i.id}.{i.get_full_name()}, id: {i.library_id}")
        return " "

    @classmethod
    def validate_reader(cls, library_id, session):
        reader = session.query(Reader).filter_by(library_id=library_id).first()
        return reader is not None

    def reviewed_books(self):
        for review in self.reviews:
            print(f"Id:{review.id} {review.book.name}")
        return " "
    
    def my_reviews(self):
        for review in self.reviews:
            print(f"{review.book.name} : {review.rating}/10")
        return " "

    @classmethod
    def add_reader(cls,first_name, last_name, library_id):
        new_row = Reader(first_name=f"{first_name}", last_name=f"{last_name}", library_id=f"{library_id}")
        session.add(new_row)
        session.commit()

    @classmethod
    def remove_reader(cls, library_id):
        rm_reader = session.query(Reader).filter(Reader.library_id == library_id).first()
        session.delete(rm_reader)
        session.commit()


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    book_id = Column(Integer(), ForeignKey('books.id'))
    reader_id = Column(Integer(), ForeignKey('readers.id'))

    book = relationship('Book', back_populates='reviews')
    reader = relationship('Reader', back_populates='reviews')

    def __repr__(self):
        return f'Review: {self.id}, ' + \
            f'Reader: {self.reader_id}, ' +\
            f'Rating: {self.rating}, ' + \
            f'Book_id: {self.book_id}'
    
    def rev_reader(self):
        query = session.query(Reader).filter_by(id = self.reader_id).first()
        return f"{query.first_name} {query.last_name}"
    
    def rev_book(self):
        query = session.query(Book).filter_by(id = self.book_id).first()
        return f"{query.name}"

    @classmethod
    def add_review(cls, rating, book_id, reader_id):
        new_row = Review(reader_id=f"{reader_id}", rating=f"{rating}", book_id=f"{book_id}")
        session.add(new_row)
        session.commit()

    @classmethod
    def all_reviews(cls):
        reviews = session.query(Review).all()
        for i in reviews:
            print(f"Review for {i.rev_book()} by {i.rev_reader()}: {i.rating}/10")
        return " "