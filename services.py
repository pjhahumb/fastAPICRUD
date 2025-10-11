from sqlalchemy.orm import Session
from schemas import Bookcreate
from models import BookModel

def insert_book(db:Session, data:Bookcreate):
    book_instance = BookModel(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_all_book(db:Session):
    return db.query(BookModel).all()
    

