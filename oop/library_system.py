# create base class Book with attributes title and author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title}, {self.author}"

# create sub_classes Ebook and PrintBook that inherit from Book
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title}, {self.author}, File Size:{self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title},{self.author}, Page Count:{self.page_count}"

# create a Library class that holds books
class Library:
    def __init__(self):
        self.books = []

    def __str__(self):
        return self.books

    def add_book(self, book):
        self.books.append(book)
        return book

    def list_books(self):
        return self.books
