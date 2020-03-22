from sqlalchemy import create_engine
engine = create_engine('sqlite:///user_v1.db', echo = True)
from user_v1 import UserModel, EndPointRpi
#from datetime import datetime, time

#from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base

   
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# a = datetime.now()

u = session.query(UserModel).filter_by(username = "titi").first()
c = EndPointRpi(rpi_name = 'powerpi_5', rpi_type = 'rpi4', rpi_IP = '10.8.0.10', user = u.id , active= True)

session.add(c)
session.commit()



