import sqlite3
from sqlite3 import Error

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# connect to db
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("E:\\books.sqlite")

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
        connection.close()
        print("SQLite DB connection closed")
    except Error as e:
        print(f"The error '{e}' occurred")

# create table
create_books_table = """ CREATE TABLE IF NOT EXISTS books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            author TEXT NOT NULL,
                            isbn INTEGER,
                            publisher TEXT
                            );
                            """
execute_query(connection, create_books_table)

# function to add a book record manually
def add_manually():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book isbn: ")
    input_add = (f"INSERT INTO books (title, author, isbn) VALUES ('{title}', '{author}', '{isbn}')")
    # change f str to dic later:
    # input_add = ("INSERT INTO books VALUES (:title, :author, :isbn)", {'title': title, 'author': author, 'isbn': isbn})
    execute_query(connection, input_add)

# delete book record
def delete_book():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    delete_row = (f"DELETE from books WHERE title = '{title}' AND author = '{author}'")
    #change f string to dic later
    execute_query(connection, delete_row)


# amend book record
def update_title():
    old_title = input("Enter old title: ")
    new_title = input("Enter new title: ")
    change_title = (f"UPDATE books SET title = '{new_title}' WHERE title = '{old_title}'")
    # change f string to dic later
    execute_query(connection, change_title)

def update_author():
    old_author = input("Enter old author name: ")
    new_author = input("Enter new new author name: ")
    change_author = (f"UPDATE books SET author = '{new_author}' WHERE author = '{old_author}'")
    # change f string to dic later
    execute_query(connection, change_author)

def update_isbn():
    old_isbn = input("Enter old isbn: ")
    new_isbn = input("Enter new isbn: ")
    change_isbn = (f"UPDATE books SET isbn = '{new_isbn}' WHERE isbn = '{old_isbn}'")
    # change f string to dic later
    execute_query(connection, change_isbn)



