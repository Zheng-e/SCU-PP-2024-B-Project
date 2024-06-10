# library.py
from book import Book

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn, quantity):
        new_book = Book(title, author, isbn, quantity)
        self.books.append(new_book)

    def view_books(self):
        return self.books

    def search_books(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower()]
