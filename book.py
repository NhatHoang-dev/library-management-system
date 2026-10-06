class Book:
    def __init__(self, title, author, isbn):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

    def __str__(self):
        status = "borrowed" if self.is_borrowed else "available"
        return f"Title: {self.title} | Author : {self.author} | status: {status}"
