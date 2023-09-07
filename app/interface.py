#!/usr/bin/env python3
from models import Base, Book, Review, Reader

if __name__ == '__main__':
    pass

name = input("Admin or Reader:")
print('Hello ' + name + '!')

if name == "Admin":
    password = input("Enter password: ")
    if password == "1234":
        print('Welcome Admin!')
        choice = input("Books or Readers: ")
        if choice == "Books":
            print(Book.all_books())
        else:
            print(Reader.all_readers())
else:
    if name == "Reader":
        full_name = input("Enter full name: ")
        print('Welcome ' + full_name + '!')
