from fastapi import FastAPI, Depends
from schemas import Bookcreate
from sqlalchemy.orm import Session
from db import get_db
from services import insert_book, get_all_book

app = FastAPI()

@app.post('/create', response_model=Bookcreate)
async def store_book(data:Bookcreate, db:Session=Depends(get_db)):
    return insert_book(db, data)

@app.post('/get_boooks', response_model=list[Bookcreate])
async def get_book(db:Session=Depends(get_db)):
    return get_all_book(db)

