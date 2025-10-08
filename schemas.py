from pydantic import BaseModel

class BookBase(BaseModel):
    title:str
    description:str
    author:str
    year:int

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id:int

    # to serialize the data
    class config:
        # orm_mode = True pydantic version <2
        form_attributes = True    