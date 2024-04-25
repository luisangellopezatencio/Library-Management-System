from models import Book, User
from colorama import Fore

class db_admin:
    def __init__(self):
        self.books = []
        self.users = []
    
    def add_book(self, title, author, year):
        new_book = Book(id=len(self.books) + 1, title=title, author=author, year=year)
        self.books.append(new_book)
        print(Fore.GREEN + "Book added successfully!")

    def show_books(self):
        if len(self.books) == 0:
            print(Fore.RED + "No books found.")
        else:
            for book in self.books:
                print(f"Title: {book.title}, Author: {book.author}, Year: {book.year}")