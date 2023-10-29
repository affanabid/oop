class Book:

    def __init__(self, name, author, price:float, qtyInStock=0):
        self.__name = name
        self.__author = Author(author, f'{author}@gmail.com', 'male')
        self.__price = max(0,price)
        self.__qtyInStock = max(0, qtyInStock)

    def getName(self):
        return self.__name
    
    def getAuthor(self):
        return self.__author
    
    def getPrice(self):
        return self.__price
    
    def setPrice(self, new_price:float):
        self.__price = new_price

    def getQtyInStock(self):
        return self.__qtyInStock
    
    def setQtyInStock(self, new_qty):
        self.__qtyInStock = new_qty

    def getAuthorName(self):
        author_object = self.getAuthor()
        author_name = author_object.name
        return author_name
    
    def print(self):
        print(f'"{self.getName()}" by {self.getAuthorName()} ({self.getAuthor().gender}) @{self.getAuthor().email}')

class Author:

    def __init__(self, name, email, gender) -> None:
        self.name = name
        self.email = email
        self.gender = gender 

book = Book('mybook', 'affan', 20.0, 5)
book = Book('mybook', 'affan', 20.0, 4)

# print(book.getAuthor())
book.setPrice(10)
print(book.getPrice())
print(book.getAuthorName())
book.print()