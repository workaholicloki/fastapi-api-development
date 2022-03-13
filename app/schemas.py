from datetime import datetime
from pydantic import BaseModel, EmailStr
from typing import Optional

class Login(BaseModel):
    email: EmailStr
    password: str

class Userout(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True

class UsersBase(BaseModel):
    name: str
    occupation: Optional[str] = ""
    age: int

class Signup(BaseModel):
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
    id: int
    createdby: Userout
    class Config:
        orm_mode = True