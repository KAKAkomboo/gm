
class Book:
    def __init__(self, title, year, author, isbn):
        self.title = title
        self.year = year
        self.author = author
        self.isbn = isbn

class Reader:
    def __init__(self, name, contact, card_num):
        self.name = name
        self.contact = contact
        self.card_num = card_num
        print(f"Reader`s name: {self.name}, Contact: {self.contact}, Library card number: {self.card_num}")

class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book {book.title} was added")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"The book with ISBN {book.isbn} was removed")
                return

    def find_book_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"The book {book.title} was found:\n Title: {book.title}, Year: {book.year}, Author: {book.author}, ISBN: {book.isbn}")
                return book

    def find_book_author(self, author):
        for book in self.books:
            if book.author.lower() == author.lower():
                print(f"Books that were found with this author {book.author}:\n Title: {book.title}, Year: {book.year}, Author: {book.author}, ISBN: {book.isbn}")
                return book

class Borrowing:

    def __init__(self, reader, book, days = 21):
        self.reader = reader
        self.book = book
        self.days = days

        print(f"The book {book.title} was borrowed by {reader.name}. The book must be returned within {days}")


class IlustratedBook(Book):

    def __init__(self,title, year, author, isbn, illustrator, illustrations_count):
        super().__init__(title, year, author, isbn)
        self.illustrator = illustrator
        self.illustrations_count = illustrations_count

    def show_info(self):
        print(f"The illustrator of {self.title} is {self.illustrator}. Number of illustrations: {self.illustrations_count}")


book1 = Book("The Witcher. Last wish", "1993", "Andrzej Sapkowski", "9786171283510")
book2 = Book("The Creative Gene", "2021", "Hideo Kojima", "9781974725915")
book3 = Book("A Song of Ice and Fire. Book 1: A Game of Thrones", "2011", "George Martin", "9789669482716")
book4 = IlustratedBook("The Vinland Saga. Volume 1", "2022", "Makoto Yukimura", "9786177678884", "Makoto Yukimura", "228")

user = Reader("Lina", "934857669", "23453")

catalog = Catalog()

catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)
catalog.add_book(book4)

catalog.remove_book("9789669482716")
catalog.find_book_title("the creative gene")
catalog.find_book_author("andrzej sapkowski")

borrowing = Borrowing(user, book2)
book4.show_info()
