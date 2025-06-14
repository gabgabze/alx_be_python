class Book:
    def __init__(self,title,author,_is_checked_out=False):
        self.title=title     # public attribute
        self.author=author   # public attribute
        self._is_checked_out = _is_checked_out # this underscore shows it is private

"""implement library class"""
class Library:
    def __init__(self, books=None):
        if books is None:
            books = []
        self._books = books

    """add methods for this operation"""
    def add_book(self,book):
        self._books.append(book)
        return f'Book "{book.title}" added to the library.'

    def checkout_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out == True:
                return book

    def return_book(self, title):
        for book in self._books:
            if book.title == title and isinstance(book,Book):
                return book


    def list_available_books(self):
        for book in self._books:
            if not book._is_checked_out:
                return



