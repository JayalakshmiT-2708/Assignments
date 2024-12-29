class Book:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price
    def display_details(self):
        print(f"Book Name: {self.book_name}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")
book1 = Book("To Kill a Mockingbird", "Harper Lee", 15.99)
book1.display_details()