from db import Base
from sqlalchemy import String, Integer, Column

class BookModel(Base):
    __tablename__ = 'Books'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True)
    desc = Column(String, index=True)
    year = Column(Integer)