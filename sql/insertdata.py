from sqlalchemy import create_engine
engine = create_engine('sqlite:///date.db', echo = True)
from models import Test1
from datetime import datetime, time

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

   
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# a = datetime.now()
y = 2019
m = 5
day = 29
e = 14
d = 40

c = datetime(y, m, day, e, d)


c1 = Test1(name = 'lacika1', address = 'Statd Nanded', email = 'ra@gmail.com', date = c)

session.add(c1)
session.commit()



