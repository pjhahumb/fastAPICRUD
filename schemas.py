from pydantic import BaseModel

class Bookbase(BaseModel):
    title:str
    author:str
    desc:str
    year:int

class Bookcreate(Bookbase):
    pass

class Book(Bookbase):
    id:int
    class config:
        form_attributes=True