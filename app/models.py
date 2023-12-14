from sqlalchemy import Column, Integer, String, Text
from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    avatar_url = Column(String)
    bio = Column(Text)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)


