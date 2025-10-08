from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# userName+password+server+port+databaseName
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/bookStore"

# to help us connect with postgres url that we defined above
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# help us perform actions on our DB, until we aren't speciying the changes we can to commit
#  in db, those changes will not be reflected in DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# to create tables
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()