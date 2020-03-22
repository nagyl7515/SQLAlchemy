from sqlalchemy import create_engine
from user import UserModel, EndPointRpi
from user import Base
engine = create_engine('sqlite:///user.db', echo = True)


Base.metadata.create_all(engine)


