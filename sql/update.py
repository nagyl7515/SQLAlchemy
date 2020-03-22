from sqlalchemy import create_engine
from models import Test1
from datetime import time

engine = create_engine('sqlite:///date.db', echo = True)




from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
result = session.query(Test1).get(3)

result.name = 'Lacko'
session.commit()

result = session.query(Test1).get(1)

print (result.name)
