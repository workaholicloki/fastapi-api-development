from passlib.context import CryptContext
from tkinter.tix import AUTO

pwd_context = CryptContext(schemes=["bcrypt"], deprecated=AUTO)
def hash(password: str):
    return pwd_context.hash(password)

