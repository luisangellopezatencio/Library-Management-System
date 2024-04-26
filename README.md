
# Library Management System

A terminal app to manage a library, allowing admins to add, search, borrow, and return books to users who have been previously registered. Additionally, admins can view registered users and register new users.


## Installation

Install Library-Management-System

```bash
  git clone https://github.com/luisangellopezatencio/Library-Management-System.git
  pip install -r requirements.txt
```
    
## Demo

<img src="https://i.imgur.com/HpqiCdy.gif" alt="Demo">

## Documentation

### Library Management System Menu
=====================================

## 1. Add Book
### Description
Add a new book to the library's collection.

### Functionality
* Prompts the book to enter book's title, author, and year of publication.
* Creates a new `Book` object with the provided information.
* Adds the new book to the library's collection.

## 2. Show Books
### Description
Display a list of all books in the library's collection.

### Functionality
* Retrieves the list of books from the library's collection.
* Displays the list of books in a readable format, including title, author, and year of publication.

## 3. Add User
### Description
Add a new user to the library's system.

### Functionality
* Prompts the user to enter the user's name and ID.
* Creates a new `User` object with the provided information.
* Adds the new user to the library's system.

## 4. Show Users
### Description
Display a list of all users in the library's system.

### Functionality
* Retrieves the list of users from the library's system.
* Displays the list of users in a readable format, including name and ID.

## 5. Borrow Book
### Description
Allow a user to borrow a book from the library's collection.

### Functionality
* Prompts the user to enter the book's title and their ID.
* Checks if the book is available and the user is eligible to borrow.
* Updates the book's status to "borrowed" and adds it to the user's borrowed books list.

## 6. Show Borrowed Books
### Description
Display a list of all borrowed books in the library's system.

### Functionality
* Retrieves the list of borrowed books from the library's system.
* Displays the list of borrowed books in a readable format, including title, author, and borrower's name.

## 7. Return Book
### Description
Allow a user to return a borrowed book to the library's collection.

### Functionality
* Prompts the user to enter the book's title and their ID.
* Checks if the book is borrowed by the user and updates its status to "available".
* Removes the book from the user's borrowed books list.

## 8. Exit
### Description
Exit the library management system and save any changes to the data.

### Functionality
* Saves any changes made to the library's collection and user data.
* Exits the program.

Note: When exiting the program using ctrl+c command instead opcion 8, any unsaved changes will be lost. It is recommended to save changes regularly to avoid data loss.
