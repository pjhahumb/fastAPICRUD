from fastapi import FastAPI, Depends
from schemas import Book, Create_Book
from sqlalchemy.orm import Session
from db import get_db
from services import create_book, get_books

app = FastAPI()

@app.post('/create', response_model=Book)
async def create(data:Create_Book, db:Session=Depends(get_db)):
   return create_book(db,data)

@app.get('/get_books', response_model=list[Book])
async def get(db:Session=Depends(get_db)):
   return get_books(db)