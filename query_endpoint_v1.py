from sqlalchemy import create_engine
from user_v1 import EndPointRpi
from datetime import time

engine = create_engine('sqlite:///user_v1.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(EndPointRpi).all()


for row in result:
   print ("Name: ",row.rpi_name, "Type:",row.rpi_type, "RPI_IP:",row.rpi_IP, "User", row.user, "Active:", row.active)

# query két feltétel szerint, aktive keresése
active = session.query(EndPointRpi).filter_by(active = True, user = 2).first()
#print (active.rpi_name)

#update aktiv törlése

rpi = session.query(EndPointRpi).filter_by(active = True, user = 2).first()
rpi.active = False
session.commit()

# másik aktivá tétele



rpi = session.query(EndPointRpi).filter_by(rpi_name = "powerpi_5", user = 2).first()
rpi.active = True
session.commit()

result = session.query(EndPointRpi).all()
for row in result:
   print ("Name: ",row.rpi_name, "Type:",row.rpi_type, "RPI_IP:",row.rpi_IP, "User", row.user, "Active:", row.active)


