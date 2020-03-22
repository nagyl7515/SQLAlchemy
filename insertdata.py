from sqlalchemy import create_engine
engine = create_engine('sqlite:///user.db', echo = True)
from user import UserModel, EndPointRpi
#from datetime import datetime, time

#from sqlalchemy import Column, Integer, String
#from sqlalchemy.ext.declarative import declarative_base

   
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# a = datetime.now()


c1 = EndPointRpi(rpi_name = 'powerpi_2', rpi_type = 'rpi4', rpi_IP = '10.8.0.13')

session.add(c1)
session.commit()



