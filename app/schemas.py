from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str


class TokenData(BaseModel):
    username: str
