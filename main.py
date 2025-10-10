from fastapi import FastAPI, Depends
import schemas, services
from sqlalchemy.orm import Session
from db import get_db

app = FastAPI()

@app.post('/books/', response_model=schemas.Book)
async def create_new_book(book:schemas.BookCreate, db:Session = Depends(get_db)):
    return services.create_book(db, book)
