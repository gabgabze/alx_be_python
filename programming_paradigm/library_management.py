class Book:
    """create instance with private attribute"""
    def __init__(self,title,author,_is_checked_out):
        self.title=title
        self.author=author
        self.is_checked_out=_is_checked_out

"""implement library class"""
class Library(Book):
    def __init__(self,books):
        self.books = []

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


