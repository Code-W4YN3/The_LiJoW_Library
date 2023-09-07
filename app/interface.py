#!/usr/bin/env python3
from models import Base, Book, Review, Reader

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

    elif name == "2":
        full_name = input("Enter full name: ")
        print('Welcome ' + full_name + '!')
    else:
            print("Invalid input. Please enter 1 or 2")
            login()


if __name__ == '__main__':
    login()
