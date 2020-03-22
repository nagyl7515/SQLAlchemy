from sqlalchemy import create_engine
from models import Test1
import datetime 
import time


engine = create_engine('sqlite:///date.db', echo = True)


while True:

    from sqlalchemy.orm import sessionmaker
    Session = sessionmaker(bind = engine)
    session = Session()
    result = session.query(Test1).filter_by(name='lacika1').first()

    print (result.date)
    t = datetime.timedelta(hours=48)
    r = (result.date) + t
    z = r.strftime('%Y-%m-%d,%H:%M')
    print (z)


    #p = datetime.datetime(result.date.year, result.date.month, result.date.day,result.date.hour, result.date.minute).strftime('%Y-%m-%d,%H:%M')
    #print (p)

    c = datetime.datetime.now()
    ct = datetime.datetime(c.year, c.month, c.day, c.hour, c.minute).strftime('%Y-%m-%d,%H:%M')
    print (ct)

    #if ct == p:
        
     #   print ("egal")
    #else:
     #   print ("no egal")

    time.sleep(20)


