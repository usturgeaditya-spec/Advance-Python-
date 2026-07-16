# Simplified Library Management System using OOP in Python

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.book_id}] {self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.patron_id}] {self.name}"


class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    # Add a new book
    def add_book(self, book):
        self.books[book.book_id] = book
        print(f"Book '{book.title}' added successfully.")

    # Register a new patron
    def register_patron(self, patron):
        self.patrons[patron.patron_id] = patron
        print(f"Patron '{patron.name}' registered successfully.")

    # Borrow a book
    def borrow_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed '{book.title}'.")

    # Return a book
    def return_book(self, patron_id, book_id):
        if patron_id not in self.patrons:
            print("Patron not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        patron = self.patrons[patron_id]

        if book in patron.borrowed_books:
            patron.borrowed_books.remove(book)
            book.is_borrowed = False
            print(f"{patron.name} returned '{book.title}'.")
        else:
            print(f"{patron.name} did not borrow '{book.title}'.")

    # Display all books
    def display_books(self):
        print("\nLibrary Books:")
        for book in self.books.values():
            print(book)

    # Display all patrons
    def display_patrons(self):
        print("\nRegistered Patrons:")
        for patron in self.patrons.values():
            print(patron)


# ------------------- Main Program -------------------

library = Library()

# Add books
library.add_book(Book(101, "Python Programming", "John Smith"))
library.add_book(Book(102, "Data Structures", "Jane Doe"))
library.add_book(Book(103, "Machine Learning", "Andrew Ng"))

# Register patrons
library.register_patron(Patron(1, "Rahul"))
library.register_patron(Patron(2, "Manish"))

# Display books and patrons
library.display_books()
library.display_patrons()

# Borrow books
library.borrow_book(1, 101)
library.borrow_book(2, 102)

# Display updated books
library.display_books()

# Return a book
library.return_book(1, 101)

# Display final status
library.display_books()            