from faker import Faker
import random
from models import Book, Reader, Review, engine, Base, session

fake = Faker()

def seed_data():
    print("Clearing DB")
    session.query(Book).delete()
    session.query(Reader).delete()
    session.query(Review).delete()

    for _ in range(10): 
        book = Book(
            name=fake.unique.name(),
            author=fake.name(),
            genre=fake.word(),
            reader_count=random.randint(1, 100)
        )
        session.add(book)

    for _ in range(20): 
        reader = Reader(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            library_id=random.randint(1000, 10000)
        )
        session.add(reader)
   
    books = session.query(Book).all()
    readers = session.query(Reader).all()
    for _ in range(30):  
        book = random.choice(books)
        reader = random.choice(readers)
        review = Review(
            rating=random.randint(1, 5),
            book=book,
            reader=reader
        )
        session.add(review)
    
    session.commit()
    session.close()


if __name__ == '__main__':
    seed_data()
