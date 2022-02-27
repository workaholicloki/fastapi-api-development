from datetime import datetime
from venv import create
from pydantic import BaseModel, EmailStr
from typing import Optional

class UsersBase(BaseModel):
    id: int
    name: str
    occupation: Optional[str] = ""
    age: int

class Signup(BaseModel):
    email: EmailStr
    password: str

class Userout(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
    
    class Config:
        orm_mode = True

class Login(BaseModel):
    email: EmailStr
    password: str

class UpdateUser(UsersBase):
    pass

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class ResponseUser(UsersBase):
    class Config:
        orm_mode = True