from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int
    borrowed: bool = False

class User(BaseModel):
    id: int  # Date obligatory doe to is the DNI            
    name: str
    borrowed_books: list = [] # if doesn't exist, it will be created as an empty list