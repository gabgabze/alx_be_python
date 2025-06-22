# create base class Book with attributes title and author
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# create sub_classes Ebook and printBook that inherit from Book
class EBook(Book):
    def __init__(self, title, author,file_size):
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title, author, page_count = 0):
        super().__init__(title, author)
        self.page_count = page_count
        
# create a Library class that has all the other classes
class Library:
    pass
"""create methods in library class
   Adds a Book, EBook, or PrintBook instance to the library.
   list_books(self): Prints details of each book in the library."""
