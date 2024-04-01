'''
Classes
- Library
- Books
- User
'''

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.libId = None
        self.borrowed_books = []

    def borrowBook(self, book):
        self.borrowed_books.append(book)

    def returnBook(self, book):
        self.borrowed_books.remove(book)

class Book:
    def __init__(self, name, category):
        self.name = name
        self.category = category
    
    def __str__(self):
        return f"Book Name: {self.name}"
    
class Library:
    def __init__(self, cap):
        self.cap = cap
        self.books = []
        self.users = {}
        self.book_ctr = 0
        self.user_ctr = 0
    
    def addBook(self, name, category):
        book = Book(name, category)
        self.books.append(book)

    def registerUser(self, user):
        self.user_ctr += 1
        self.users[self.user_ctr] = user
        user.id = self.user_ctr

    def displayBooks(self):
        for book in self.books:
            print(book)
    