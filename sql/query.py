from sqlalchemy import create_engine
from models import Test1
from datetime import time

engine = create_engine('sqlite:///date.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Test1).all()


for row in result:
   print ("Name: ",row.name, "Address:",row.address, "Email:",row.email, "Date:", time(row.date.hour, row.date.minute).strftime('%H:%M')
 )