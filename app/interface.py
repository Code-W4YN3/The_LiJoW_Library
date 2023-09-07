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
                        print(" \nAll Books: ")
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
                        print(" \nAll Readers: ")
                        print(Reader.all_readers())
                        choice = input("Select \n1.Remove Reader \n2.Back \nInput: ")
                        if choice == "1":
                            print("Enter: ")
                            lib_id = input("Library Id: ")
                            Reader.remove_reader(lib_id)
                            print(f"Removed book by id {lib_id} \n ")
                            admin_choice()
                        elif choice == "2":
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

    elif name == "2":
        library_id = int(input("Enter Library ID: "))
        if Reader.validate_reader(library_id, session):
            # Get reader data for logged reader through  their associated table row
            logged_reader = session.query(Reader).filter(Reader.library_id == library_id).first()
            print(f' \nWelcome {logged_reader.get_full_name()}!')

            def reader_choice():
                choice = input("Navigate to: \n1.All Books \n2.All Reviews \n3.Logout \nInput: ")
                if choice == "1":
                    print(" \nAll Library Books: ")
                    print(Book.all_books())
                    choice = input("Navigate to: \n1.Add Review \n2.Read Books \n3.Back \nInput: ")
                    if choice == "1":
                        print("Enter: ")
                        rating = int(input("Rating(1-10): "))
                        bk_id = int(input(f"Book ID(1-{session.query(Book).count()}): "))
                        reader_id = logged_reader.id
                        if((0 < rating <= 10) and (0 < bk_id <= session.query(Book).count())):
                            Review.add_review(rating, bk_id, reader_id)
                            print(f"Added review {rating} {bk_id} {reader_id}\n ")
                            reader_choice()
                        else:
                            print("Please enter values within valid range.")
                            reader_choice()
                    elif choice == "2":
                        print(" \nMy Read Books: ")
                        print(logged_reader.reviewed_books())
                        choice = input("Select: \n1.Back")
                        if choice == "1":
                            reader_choice()
                        else:
                            print("Invalid Input. Returning to Reader Menu.")
                            reader_choice()
                    elif choice == "3":
                        reader_choice()
                    else:
                        print("Invalid Input. Returning to Reader Menu")
                        reader_choice()

                elif choice == "2":
                    print(" \nAll Reader Reviews: ")
                    print(Review.all_reviews())
                    choice = input("Select: \n 1.My Reviews \n2.Back")
                    if choice == "1":
                        print(" \nMy Reviews")
                        print(logged_reader.my_reviews())
                        choice = input("Select: \n1.Back")
                        if choice == "1":
                            reader_choice()
                        else:
                            print("Invalid Input. Returning to Reader Menu.")
                            reader_choice()
                    elif choice == "2":
                        reader_choice()
                    else:
                        print("Invalid Input. Returning to Reader Menu.")
                        reader_choice()
                elif choice == "3":
                    print("Successfully logged out \n ")
                    login()

                else:
                    print("Invalid Input. Please select 1, 2 or 3")
                    reader_choice()

            reader_choice()
        else:
            print(f" \nReader '{library_id}' does not exist.")
            choice = input("Navigate to: \n1.Add Reader \n2.Logout \nInput: ")
            if choice == "1":
                print("Enter: ")
                f_name = input("First Name: ")
                l_name = input("Last Name: ")
                lib_id = library_id  # Assigns Library ID to the initially entered id
                Reader.add_reader(f_name, l_name, lib_id)
                print(f"Added reader {f_name} {l_name} {lib_id}\n ")
                login()

            elif choice == "2":
                print("Successfully logged out")
                login()

            else:
                print("Invalid Input. Returning to login menu.")
                login()


       
    else:
        print("Invalid input. Please enter 1 or 2")
        login()

if __name__ == '__main__':
    login()
