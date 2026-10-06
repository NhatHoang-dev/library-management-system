from book import Book
from member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def find(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def lend_book(self, title, member):
        book = self.find(title)
        if book:
            if not book.is_borrowed:
                book.borrow()
                member.borrow_book(book)
                print(f"Member {member.name} has successfully borrowed '{book.title}'.")
            else:
                print(f"'{book.title}' is already borrowed.")
        else:
            print(f"'{title}' is not available in the library.")

    def return_book(self, title, member):
        book = self.find(title)
        if book:
            if book in member.borrowed_books:
                book.return_book()
                member.return_book(book)
                print(f"Member {member.name} has successfully returned '{book.title}'.")
            else:
                print(f"Member {member.name} has not borrowed '{book.title}'.")
        else:
            print(f"'{title}' is not available in the library.")


if __name__ == "__main__":
    my_library = Library()

    book1 = Book(title="The Power of Now", author="Eckhart Tolle", isbn=123456)
    book2 = Book("Why We Sleep", "Matthew Walker ", 123233)
    book3 = Book("Sleep Smarter ", "J. Allan Hobson", 193982)

    print(book1)

    member1 = Member("Minh", "DS210321")
    member2 = Member("Hoang", "DS210440")
    print(member1)

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.lend_book("Why We Sleep", 
                         member1)
    my_library.lend_book("The Truth About Dreams", member2)
    my_library.return_book("Sleep Smarter", member1)
    my_library.return_book("Sleep Smarter", member2)