import os
from colorama import Fore, Style, init
from typing import Tuple
from database import db_admin


# initialize colorama and instantiate the database
init(autoreset=True)
db_admin = db_admin()

class App:
    """
    This is the main menu for the library management system
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
        3. Borrow book
        4. Add user
        5. Show users
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
                return True
            elif user_input == 2:
                self.show_books()
                return True
            elif user_input == 8:
                return False