class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    def borrow_book(self, book):
        self.borrowed_books.append(book)
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
    def __str__(self):
        return f"member {self.name} | member_id: {self.member_id} | borrowed: {len(self.borrowed_books)} book"
