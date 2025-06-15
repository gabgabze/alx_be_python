class Book:

    """create instance with private attribute"""
    def __init__(self,title,author, is_checked_out):
        self.is_checked_out = is_checked_out
        self.title = title
        self.author = author

"""implement library class"""
class Library:
    def __init__(self,books):
        self.books = books

    """add methods for this operation"""
    def add_book(self, book):
        self.books.append(book)
        return self

    def checkout_book(self, title):
        for book in self.books:
            if book.title == title:
                return book

    def list_available_books(self):
        return self.books


