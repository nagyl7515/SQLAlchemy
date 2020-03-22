from sqlalchemy import create_engine
from models import Test1
from models import Base
engine = create_engine('sqlite:///date.db', echo = True)






Base.metadata.create_all(engine)


