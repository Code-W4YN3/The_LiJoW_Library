# The_LiJoW_Library
#### This is a Library Management System created using Python and SQLAlchemy.
#### By Linet Muthii, Joanne Ndirangu and Wayne Otido

Project presentation slides: 
https://docs.google.com/presentation/d/e/2PACX-1vSNm3ne5cInyCdGLdlX1ruqN5VOWSI6V7HHwU9A8IlZFAMDeSDse3me0dgX9kJhu-cPpIzSDQHFOtVm/pub?start=true&loop=false&delayms=10000&slide=id.gc6f90357f_0_5

## Description
A library project ,using CLI for user input, that manages the library database, book, reader and reader-review tables.

### Core Deliverables:
Select my type of user account; Admin or Reader
An admin should be able to:
* Log in
* View all books
* Add or Remove books
* View all readers
* Remove readers
* Log out

As a user i should be able to:
* Log in or Register
* See a list or books in the library
* Add a review 
* View my read books
* View other reader reviews
* View my reviews
* Log out


## Run Locally
### Setup/Installation Requirements
To run this app locally, you need a PC with:
* Access to the internet

### Installation Process
  1. Clone this repository using
    ```bash
      git clone git@github.com:Code-W4YN3/The_LiJoW_Library.git
    ```
  2. Navigate into the project folder.
    ```bash
      cd The_LiJoW_Library
    ```
  3. Run the following commands in the terminal:
    ```
      pipenv install
    ```
    to install dependencies
  4. Run the command:
    ```
      pipenv shell
    ```
    to enter a virtual python environment
  5. Switch to the "app" directory using the command:
    ```
      cd app/
    ```
  6. Execute the command:
    ```
      python3 interface.py
    ```
    to run the CLI application

# Technologies used
  * Python
  * SQLAlchemy
