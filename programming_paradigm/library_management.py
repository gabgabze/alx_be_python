class Book:
    def __init__(self,title,author,_is_checked_out):
        self.title=title     # public attribute
        self.author=author   # public attribute
        self._is_checked_out = True # this underscore shows it is private

"""implement library class"""

class Library:
    def __init__(self, _books):
        self._books = []

    """add methods for this operation"""
    def add_book(self, _books):
        self._books.append(_books)

    def checkout_book(self, title):
        for book in self._books:
            if book.title == title:
                return book

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book

    def list_available_books(self):
        return self.books


