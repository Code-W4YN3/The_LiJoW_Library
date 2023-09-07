#!/usr/bin/env python3
from models import Base, Book, Review, Reader
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def login():
    name = input("Please select: \n1.Admin \n2.Reader\nInput: ")

    if name == "1":
        print(' \nHello Admin!')
        def admin():
            password = input("  \n Enter password: ")
            if password == "1234":
                print('  \nWelcome Admin!')
                def admin_choice():
                    choice = input("Navigate to: \n1.All Books \n2.All Readers \n3.Logout \nInput: ")
                    if choice == "1":
                        print(Book.all_books())
                        choice = input("Select \n1.Add Book \n2.Remove Book \n3.Back \nInput: ")
                        if choice == "1":
                            print("Enter: ")
                            bk_name = input("Book Name: ")
                            bk_author =input("Author: ")
                            bk_genre = input("Genre: ")
                            Book.add_book(bk_name, bk_author, bk_genre)
                            print(f"Added book {bk_name} by {bk_author} \n ")
                            admin_choice()

                        elif choice == "2":
                            print("Enter: ")
                            bk_id = input("Book Id: ")
                            Book.remove_book(bk_id)
                            print(f"Removed book by id {bk_id} \n ")
                            admin_choice()

                        elif choice == "3":
                            admin_choice()
                        else:
                            print(" \nInvalid input. Please enter 1, 2 or 3")
                            admin_choice()
                    elif choice == "2":
                        print(Reader.all_readers())
                        choice = input("Select \n1.Add Reader \n2.Remove Reader \n3.Back \nInput: ")
                        if choice == "1":
                            pass
                        elif choice == "2":
                            pass
                        elif choice == "3":
                            admin_choice()
                        else:
                            print(" \nInvalid input. Please enter 1, 2 or 3")
                            admin_choice()

                    elif choice == "3":
                        print("Successfully logged out")
                        login()

                    else:
                        print("Invalid input. Please enter 1 or 2")
                        admin_choice()
                admin_choice()

            else:
                print("Incorrect password\n ")
                login()
        admin()


    if name == "2":
        library_id = int(input("Enter Library ID: "))
        if Reader.validate_reader(library_id, session):
            print(f"Reader with Library ID '{library_id}' exists.")
        else:
            print(f"Reader '{library_id}' does not exist.")
            choice = input("Navigate to: \n1.Add Reader \n2.Logout \nInput: ")
            if choice == "1":
                print("Enter: ")
                f_name = input("First Name: ")
                l_name = input("Last Name: ")
                lib_id = int(input("Library: "))  # Convert to integer
                Reader.add_reader(f_name, l_name, lib_id)
                print(f"Added reader {f_name} {l_name} {lib_id}\n ")

            else:
                print("Successfully logged out")
                login()

        print(f'Welcome {library_id}!')

        def reader_choice():
            choice = input("Navigate to: \n1.All Books \n2.Read Books \n3.Logout \nInput: ")
            if choice == "1":
                print(Book.all_books())
                choice = input("Navigate to: \n1.Add Review \n2.Logout \nInput: ")
                if choice == "1":
                    print("Enter: ")
                    rating = int(input("Rating: "))
                    bk_id = int(input("Book ID: "))
                    reader_id = int(input("Reader ID: "))
                    Review.add_review(rating, bk_id, reader_id)
                    print(f"Added review {rating} {bk_id} {reader_id}\n ")

            elif choice == "2":
                print("")

            else:
                print("Successfully logged out")
                login()

        reader_choice()
    else:
        print("Invalid input. Please enter 1 or 2")
        login()

if __name__ == '__main__':
    login()
