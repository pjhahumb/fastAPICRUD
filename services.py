from sqlalchemy.orm import Session
from schemas import Create_Book
from models import BookModel
def create_book(db:Session, data:Create_Book):
    book_instance = BookModel(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db:Session):
    return db.query(BookModel).all()