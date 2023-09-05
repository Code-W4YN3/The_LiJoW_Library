from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Book, Reader, Review, engine, session

fake = Faker()

if __name__ == '__main__':
    pass


session.close()