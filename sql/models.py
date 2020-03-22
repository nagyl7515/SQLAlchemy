from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Test1(Base):
   __tablename__ = 'test'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   address = Column(String)
   email = Column(String)
   date = Column(DateTime)