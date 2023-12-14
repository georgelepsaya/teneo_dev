from fastapi import Depends, Form
from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str

