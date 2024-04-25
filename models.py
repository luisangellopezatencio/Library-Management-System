from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    borrowed: bool = False

class User(BaseModel):
    id: int              # id is the personal document such as DNI, passport, etc
    name: str
    borrowed_books: list = [] # if doesn't exist, it will be created as an empty list