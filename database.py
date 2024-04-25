from models import Book, User
from colorama import Fore
import json
from terminaltables import AsciiTable

class db_admin:
    def __init__(self):
        self.books = []
        self.users = []

    def load_data_json(self, path: str = "data.json"):
        try:
            with open(path, "r") as file:
                library_data = json.load(file)
                self.books = [Book(**book) for book in library_data["Books"]]
                self.users = [User(**user) for user in library_data["Users"]]
            print(Fore.GREEN + "Data loaded successfully!")
        except IOError as e:
            print(f"{Fore.RED} Error reading from file: {e}")
    
    def add_book(self, title, author, year):
        new_book = Book(id=len(self.books) + 1, title=title, author=author, year=year)
        self.books.append(new_book)
        print(Fore.GREEN + "Book added successfully!")

    def show_books(self):
        if len(self.books) == 0:
            print(Fore.RED + "No books found.")
        else:
            table_data = [["id", "Title", "Author", "Year", "Borrowed"]]
            for book in self.books:
                table_data.append([book.id, book.title, book.author, book.year, book.borrowed])
            table = AsciiTable(table_data, "Books")
            print(table.table)
    
    def add_user(self, name: str, id_card: int):
        new_user = User(id=id_card, name=name)
        self.users.append(new_user)
        print(Fore.GREEN + "User added successfully!")
    
    def show_users(self):
        if len(self.users) == 0:
            print(Fore.RED + "No users found.")
        else:
            table_data = [["id", "Name"]]
            for user in self.users:
                table_data.append([user.id, user.name])
            table = AsciiTable(table_data, "Users")
            print(table.table)

    def borrow_book(self, user_id: int, book_id: int):
        for user in self.users:
            if user.id == user_id:
                for book in self.books:
                    if book.id == book_id:
                        if book.borrowed:
                            print(Fore.RED + "Book already borrowed.")
                        else:
                            book.borrowed = True
                            user.borrowed_books.append(book)
                            print(Fore.GREEN + "Book borrowed successfully to user: " + user.name + "!")
                        return
                print(Fore.RED + "Book not found.")
                return
        print(Fore.RED + "User not found.")
    
    def show_borrowed_books(self):
        if len(self.users) == 0:
            print(Fore.RED + "No users found.")
        else:
            table_data = [["id", "Title", "Author", "Year", "Borrower", "User ID"]]
            for user in self.users:
                for book in user.borrowed_books:
                    table_data.append([book.id, book.title, book.author, book.year, user.name, user.id])
            table = AsciiTable(table_data, "Borrowed Books")
            print(table.table)
    
    def show_available_books(self):
        available_books = []
        for book in self.books:
            if not book.borrowed:
                available_books.append(book)
        if len(available_books) == 0:
            print(Fore.RED + "No available books.")
        else:
            table_data = [["id", "Title", "Author", "Year"]]
            for book in available_books:
                table_data.append([book.id, book.title, book.author, book.year])
            table = AsciiTable(table_data, "Available Books")
            print(table.table)

    def return_book(self, user_id: int, book_id: int):
        for user in self.users:
            if user.id == user_id:
                for book in user.borrowed_books:
                    if book.id == book_id:
                        book.borrowed = False
                        for book_ in self.books:
                            if book_.id == book_id:
                                book_.borrowed = False
                        user.borrowed_books.remove(book)
                        print(Fore.GREEN + "Book returned successfully!")
                        return
                print(Fore.RED + "Book not borrowed.")
                return
        print(Fore.RED + "User not found.")
    
    def save_data_json(self):
        # I saved the data in a json file because I will integrate it with an API using fastapi
        # and mongoDB
        library_data = {
            "Books": [book.dict() for book in self.books],
            "Users": [user.dict() for user in self.users]
        }

        try:
            with open("data.json", "w") as file:
                json.dump(library_data, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}")
        finally:
            file.close()
