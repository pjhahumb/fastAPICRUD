from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql://postgres:password@localhost:5432/bookStore'

engine = create_engine(DATABASE_URL)

localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

def create_table():
    base.metadata.create_all(bind=engine)