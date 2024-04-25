import os
from colorama import Fore, Style, init
from typing import Tuple
from database import db_admin


# initialize colorama and instantiate the database
init(autoreset=True)
db_admin = db_admin()

class App:
    """
    This is the logic for the library management system
    - show the options
    - get the user input
    - validate the user input
    - execute the selected option
    """
    def __init__(self, trigger: bool):
        # trigger is used to know if the menu should be shown and to stop the loop
        self.trigger = trigger

    def Menu_show(self):

        print(Fore.MAGENTA + "Welcome to Library Management System")
        print("""
        1. Add book
        2. Show books
        3. Add user
        4. Show users
        5. Borrow book
        6. Show borrowed books
        7. Return book
        8. Exit
        """)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def get_user_input(self) -> Tuple[int, bool]:
        """
        get the user input
        return the user input and True if the input is valid else False

        args: None
        return: user_input: int, valid: bool
        """
        try:
            user_input = int(input(Fore.GREEN + "Enter your option: " + Style.RESET_ALL))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a integer number between 1 and 8." + Style.RESET_ALL)
            return self.get_user_input() # recursive call to get_user_input if input is invalid

        return user_input, self.validate_user_input(user_input)

    def validate_user_input(self, user_input: int) -> bool:
        """
        validate the user input

        args: user_input: int
        return: True if the input is valid else False
        """
        if user_input > 0 and user_input < 9:
            return True
        else:
            return False
    
    def add_book(self):
        title = input("Enter the title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the year: "))
        db_admin.add_book(title, author, year)

    def show_books(self):
        db_admin.show_books()
    
    def add_user(self):
        name = input("Enter the name: ")
        id_card = int(input("Enter the your number of identification(CC, NIE, DNI): "))
        db_admin.add_user(name, id_card)
    
    def show_users(self):
        db_admin.show_users()
    
    def borrow_book(self):
        print("Showing available books:")
        db_admin.show_available_books()
        book_id = int(input("Enter the id of the book you want to borrow: "))
        user_id = int(input("Enter the id of the user: "))
        db_admin.borrow_book(user_id, book_id)

    def show_borrowed_books(self):
        print("Showing borrowed books:")
        db_admin.show_borrowed_books()

    def return_book(self):
        print("Showing borrowed books:")
        db_admin.show_borrowed_books()
        book_id = int(input("Enter the id of the book you want to return: "))
        user_id = int(input("Enter the id of the user: "))
        db_admin.return_book(user_id, book_id)

    def execute_option(self, user_input: int, valid: bool) -> bool:

        """
        This function executes the selected option and controls the loop
        through the trigger
        
        args: user_input: int, valid: bool
        return: True if the option is valid else False
        """

        if not valid:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 8." + Style.RESET_ALL)
        else:
            if user_input == 1:
                self.add_book()
            elif user_input == 2:
                self.show_books()
            elif user_input == 3:
                self.add_user()
            elif user_input == 4:
                self.show_users()
            elif user_input == 5:
                self.borrow_book()
            elif user_input == 6:
                self.show_borrowed_books()
            elif user_input == 7:
                self.return_book()
            elif user_input == 8:
                print("Saving database changes...")
                db_admin.save_data_json()
                print(Fore.GREEN + "Database saved successfully!" + Style.RESET_ALL)
                print(Fore.GREEN + "Goodbye!" + Style.RESET_ALL)
                self.trigger = False
            
        return self.trigger