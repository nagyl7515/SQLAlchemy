from sqlalchemy import create_engine
from user_v1 import UserModel, EndPointRpi
from user_v1 import Base
engine = create_engine('sqlite:///user_v1.db', echo = True)


Base.metadata.create_all(engine)


