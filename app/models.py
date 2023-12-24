from sqlalchemy import Column, Integer, String, Text, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


user_tag_association = Table(
    "user_tag_association",
    Base.metadata,
    Column("user_id", ForeignKey("users.id")),
    Column("tag_id", ForeignKey("tags.id"))
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    avatar_url = Column(String)
    bio = Column(Text)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # relationship to the Tag model
    tags = relationship("Tag", secondary=user_tag_association, back_populates="users")


class Tag(Base):
    __tablename__ = 'tags'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)

    # relationship to the User model
    users = relationship("User", secondary=user_tag_association, back_populates="tags")
