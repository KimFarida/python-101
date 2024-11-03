from datetime import datetime


# Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        # Initialize book with title, author, ISBN, and availability status
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def display_details(self):
        # Display book details
        status = "Available" if not self.is_borrowed else "Not Available"
        print(f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}")


# Define the Borrower class
class Borrower:
    def __init__(self, borrower_id, name):
        # Initialize borrower with ID, name, and a list of borrowed books
        self.borrower_id = borrower_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        # Borrow book if conditions are met
        pass  # To be implemented

    def return_book(self, book):
        # Return book if the book is in borrowed list
        pass  # To be implemented


# Define the Transaction class
class Transaction:
    def __init__(self, book, borrower, transaction_type):
        # Initialize transaction with book, borrower, type, and date
        self.date = datetime.now()
        self.book = book
        self.borrower = borrower
        self.transaction_type = transaction_type


# Define the Library class
class Library:
    def __init__(self):
        # Initialize library with lists for books and borrowers
        self.books = []
        self.borrowers = []
        self.transactions = []

    def add_book(self, title, author, isbn):
        # Add a book to the library
        pass  # To be implemented

    def remove_book(self, isbn):
        # Remove a book by ISBN
        pass  # To be implemented

    def register_borrower(self, borrower_id, name):
        # Register a new borrower
        pass  # To be implemented

    def borrow_book(self, borrower_id, isbn):
        # Facilitate book borrowing
        pass  # To be implemented

    def return_book(self, borrower_id, isbn):
        # Facilitate book return
        pass  # To be implemented
