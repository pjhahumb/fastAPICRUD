from fastapi import FastAPI, Depends, HTTPException
import services, schemas
from db import get_db
from sqlalchemy.orm import Session

app = FastAPI()

@app.get('/books/', response_model=list[schemas.Book])
async def get_all_books(db:Session = Depends(get_db)):
    return services.get_books(db)

@app.post('/books/', response_model=schemas.Book)
async def create_new_book(book:schemas.BookCreate, db:Session = Depends(get_db)):
    return services.create_book(db, book)

@app.put('/books/{id}', response_model=schemas.Book)
def update_book(book:schemas.BookCreate, id:int, db:Session = Depends(get_db)):
    db_update = services.update_book(db, book, id)
    if not db_update:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_update

@app.delete('/books/{id}')
def delete_book(id:int, db:Session = Depends(get_db)):
    deleted = services.delete_book(db, id)
    if deleted==0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted successfully"}