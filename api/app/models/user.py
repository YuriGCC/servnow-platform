from sqlalchemy import Column, Integer, String
from api.app.db.session import Base

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    login = Column(String)
