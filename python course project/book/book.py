# book.py
class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.isbn}, Quantity: {self.quantity}"