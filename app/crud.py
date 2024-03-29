from sqlalchemy.orm import Session
from . import models


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_tags(db: Session, username: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    return user.tags
