# borrow_return.py
from book import Book

class BorrowReturn:
    def __init__(self, library):
        self.library = library
        self.borrowed_books = {}

    def borrow_book(self, isbn):
        for book in self.library.books:
            if book.isbn == isbn and book.quantity > 0:
                book.quantity -= 1
                self.borrowed_books[isbn] = self.borrowed_books.get(isbn, 0) + 1
                return f"Borrowed {book.title}"
        return "Book not available"

    def return_book(self, isbn):
        if isbn in self.borrowed_books and self.borrowed_books[isbn] > 0:
            self.borrowed_books[isbn] -= 1
            for book in self.library.books:
                if book.isbn == isbn:
                    book.quantity += 1
                    return f"Returned {book.title}"
        return "Book not borrowed"