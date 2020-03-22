from sqlalchemy import create_engine
from user_v1 import UserModel, EndPointRpi
from datetime import time
import json

engine = create_engine('sqlite:///user_v1.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(UserModel).all()



for row in result:
   print ("ID: ", row.id, "Name: ",row.username, "Password:",row.password, "Admin: ", row.admin)


user = session.query(UserModel).filter_by(username = "titi").first()  # készít egy listát ami tartalmazza a user eszközeit tuple formárumban!
#print (user.id)

#RPIs = []
l = {"ennpoints" : [i.json() for i in user.rpi]}  # kiírja a végpontokat egy listben
print(l)

"""
for i in user.rpi:
    if i.active == True:
        print(i.rpi_IP)
"""


def search_ip(arg):  # az aktiv IP kiválasztása 
    for i in arg:
        if i.active == True:
            return i.rpi_IP

ip = search_ip(user.rpi)
print(ip)


#ha a kettőből akarok lekérdezni, ki kell próbálni!!!!
#https://stackoverflow.com/questions/46141867/how-to-filter-by-multiple-criteria-in-flask-sqlalchemy/46143125

existing = User.query.join(User.spaces).filter(User.username=='Bob', Space.name=='Mainspace').first()

user = session.query(UserModel).join(EndPointsRpi).filter_by(username = "titi", EndPointsRpi.active = True ).first() 


q = (Session.query(UserModel,Document,DocumentPermissions)
    .filter(User.email == Document.author)
    .filter(Document.name == DocumentPermissions.document)
    .filter(User.email == 'someemail')
    .all())


"""
    a = (i.rpi_name, i.rpi_IP, i.active)
    print (type(a))
    RPIs.append(a)
#y = json.dumps(RPIs)
print(RPIs)


for x in RPIs:  # kiírja az alábbi nevű eszköz IP címét
    if x[0] == "powerpi_1":
            print (x[1])
 
for i in RPIs:  # kiírja az összes eszközt név szerint
    print (i[0])

def func(a, ):
    return {"name" : user.rpi_name, "ip": a[1], "active": a}

"""