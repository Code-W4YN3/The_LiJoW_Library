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
print("Book Readers: ")
print(book1.all_readers())
print("Book Total Reader-Count: ")
print(book1.total_reader_count())
print("All books: ")
print(Book.all_books())


reader1 = session.query(Reader).first()
print("Reader Name: ")
print(reader1.get_full_name())
print("Library Id: ")
print(reader1.library_id)
print("Favorite Book:")
print(reader1.favorite_book())
print("Reviewed Books: ")
print(reader1.reviewed_books())
print("All Readers: ")
print(Reader.all_readers())

review1 = session.query(Review).first()
print("Review Reader: ")
print(review1.rev_reader())
print("Review Book: ")
print(review1.rev_book())
print("All Reviews: ")
print(Review.all_reviews())