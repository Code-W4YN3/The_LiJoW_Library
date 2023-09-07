from faker import Faker
import random
from models import Book, Reader, Review, engine, Base, session

fake = Faker()

def seed_data():
    print("Clearing DB")
    session.query(Book).delete()
    session.query(Reader).delete()
    session.query(Review).delete()


    print("...")
    print("Seeding Books, Readers and Reviews...")
    genres = ["Fiction", "Romance", "Fantasy", "History", "Self-Help", "Humor"]
    for _ in range(20):
        book = Book(
            name=fake.unique.name(),
            author=fake.name(),
            genre=random.choice(genres),
            reader_count=random.randint(1, 100)
        )
        session.add(book)

    for _ in range(15):
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
            rating=random.randint(1, 10),
            book=book,
            reader=reader
        )
        session.add(review)

    print("...")
    print("Seeded data")
    session.commit()
    session.close()


if __name__ == '__main__':
    seed_data()
