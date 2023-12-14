import bcrypt
import re


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def is_password_valid(password: str) -> bool:
    # Password must be at least 8 characters and include a mix of upper and lower case letters and numbers
    return len(password) >= 8 and re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)", password)
