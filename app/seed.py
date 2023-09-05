from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, Reader, Review, engine, session

fake = Faker()

if __name__ == '__main__':
    def seed_data():
        for _ in range(20):
            book = Book(
                title=fake.catch_phrase(),
                author=fake.name(),
                publication_year=fake.random_int(min=1900, max=2023),
            )
            session.add(book)

        for _ in range(20):
            reader = Reader(
                name=fake.name(),
                email=fake.email(),
                birthdate=fake.date_of_birth(minimum_age=18, maximum_age=80),
            )
            session.add(reader)

        # Create random reviews for the books
        books = session.query(Book).all()
        readers = session.query(Reader).all()
        for _ in range(30):
            book = random.choice(books)
            reader = random.choice(readers)
            review = Review(
                rating=random.randint(1, 5),
                comments=fake.paragraph(),
                book=book,
                reader=reader,
            )
            session.add(review)

    seed_data()

    session.commit()

    session.close()