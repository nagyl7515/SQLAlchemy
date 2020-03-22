from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# minden rpi -nek több tulajdonosa 

class EndPointRpi(Base):   # ő a child
    __tablename__ = "endpoint"

    id = Column(Integer, primary_key=True)
    rpi_name = Column(String(80))
    rpi_type = Column(String(80))
    rpi_IP = Column(String(20))
    #user = relationship("UserModel", backref="endpoint", lazy='dynamic')

    user = Column(Integer, ForeignKey('users.id'))

    def __init__(self, rpi_name, rpi_type, rpi_IP, user):
        self.rpi_name = rpi_name
        self.rpi_type = rpi_type
        self.rpi_IP = rpi_IP
        self.user = user



class UserModel(Base):   # ő a parent
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    password = Column(String(80))
    #rpi = Column(Integer, ForeignKey('endpoint.rpi_name'))

    rpi = relationship("EndPointRpi", backref="users", lazy='dynamic')
    

    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def user_rpi(self):  # kiírja a userhez tartozó rpi-ket
        for i in self.rpi:
            print ("Rpi name: {} , rpi IP : {}".format(i.rpi_name, i.rpi_IP))



    

    #@classmethod
    #def username_from_id(cls):
        #userid = get_jwt_identity()
        #user_by_id = cls.query.filter_by(id = userid).first()
        #username_id = user_by_id.username
        #return username_id
#    