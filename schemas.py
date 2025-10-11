from pydantic import BaseModel

class Book_base(BaseModel):
    title:str
    author:str
    desc:str
    year:int

class Create_Book(Book_base):
    pass
class Book(Book_base):
    id:int
    class config:
        form_attributes=True