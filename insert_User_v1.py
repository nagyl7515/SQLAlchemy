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


c1 = UserModel(username = 'titi', password = 'titi')

session.add(c1)
session.commit()



