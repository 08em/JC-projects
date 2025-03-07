
class Book:
    def __init__(self, title, author, genre):
        self.__title = title
        self.__author = author
        self.__genre = genre

    def getTitle(self):
        return self.__title
    def getAuthor(self):
        return self.__author
    def getGenre(self):
        return self.__genre
    

class Library:
    def __init__(self, name, address) :
        self.__name = name
        self.__address = address
        self.__books = []
    
    def addBook(self, book):
        self.__books.append(book)

    def printLibraryBooks(self):
        for book in self.__books :
            print(book.getTitle(), book.getAuthor(), book.getGenre())


book1 = Book("alevel cs textbook", "cambridge", "non fiction")
book2 = Book("igcse cs textbook", "cambridge", "non fiction")
library1 = Library("BBS library", "BBS PIK")

library1.addBook(book1)
library1.addBook(book2)

library1.printLibraryBooks()

# polymorphism

a = 5
b = 6
c = 7

def add(a, b):
    return a + b

def add(a, b, c):
    return a + b + c

print(add(a,b))
print(add(a,b,c))