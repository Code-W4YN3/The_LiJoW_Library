from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker

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

class Reader(Base):
    __tablename__ = 'readers'

    id = Column(Integer(), primary_key=True)
    first_name = Column(String())
    last_name = Column(String())
    library_id = Column(Integer())

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    rating = Column(Integer())
    book_id = Column(Integer())
    reader_id = Column(Integer())