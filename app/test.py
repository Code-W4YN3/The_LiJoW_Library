#Test file for table methods

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Book, Review, Reader, session, engine

book1 = session.query(Book).first()
reader1 = session.query(Reader).first()
review1 = session.query(Review).first()

print("Book test cases... ")
print("Book Name: ")
print(book1.name)
print("Book Author: ")
print(book1.author)
print("Book Genre: ")
print(book1.genre)
print("Book Reviews: ")
print(book1.all_reviews())
print("Book Total Reader-Count: ")
print(book1.total_reader_count())
