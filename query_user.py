from sqlalchemy import create_engine
from user import UserModel
from datetime import time
import json

engine = create_engine('sqlite:///user.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(UserModel).all()


#for row in result:
   #print ("ID: ", row.id, "Name: ",row.username, "Password:",row.password)


user = session.query(UserModel).filter_by(username = "laci").first()
#print (user.id)
RPIs = {}
for i in user.rpi:
   RPIs[i.rpi_name] = i.rpi_IP
print (RPIs)
#user.user_rpi()
y = json.dumps(RPIs)
print(y)