
class Book_A3:
    def __init__(self, title, author, price):
        # This is a parameterized constructor
        self.title = title
        self.author = author
        self.price = price

    def details(self):
        print(f"Book Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

book1_a3 = Book_A3("Python Programming", "John Doe", 25.99)
book1_a3.details()
