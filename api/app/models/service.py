from sqlalchemy import Column, Float, Integer, String
from api.app.db.session import Base

class Service(Base):
    __tablename__ = 'Service'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    price = Column(Float)


