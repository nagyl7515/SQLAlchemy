from sqlalchemy import create_engine
from user import EndPointRpi
from datetime import time

engine = create_engine('sqlite:///user.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(EndPointRpi).all()


for row in result:
   print ("Name: ",row.rpi_name, "Type:",row.rpi_type, "RPI_IP:",row.rpi_IP, "User", row.user)
 