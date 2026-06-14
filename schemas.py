from typing import Union
from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: Union[str, None] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    author_id: str
    class Config:
        from_attributes = True

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class Author(AuthorBase):
    id: int
    books: list[Book] = []
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    login: str

class UserDB(UserBase):
    password: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        from_attributes = True

