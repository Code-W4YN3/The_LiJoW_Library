from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.associationproxy import association_proxy

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
    customers = association_proxy('reviews', 'reader',
        creator=lambda rd: Review(reader=rd))
    
    def __repr__(self):
        return f"Book {self.id}: " \
            + f"Name: {self.name}, " \
            + f"Author: {self.author}"\
            + f"Genre: {self.genre}" \
            + f"Readers: {self.reader_count}"


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