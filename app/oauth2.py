from pyexpat import model
from fastapi import status, HTTPException
from fastapi import Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "24276c8fafd6146cfc45abef146fd0555fc946a15852643c59e24b4c33f22ad4"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_access_token(token: str, crendential_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise crendential_exception
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise crendential_exception
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db : Session = Depends(database.get_db)):
    crendential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials", headers={"WWW-Authenticate":"Bearer"})
    token  = verify_access_token(token, crendential_exception)
    user = db.query(models.Users).filter(models.Users.id == token.id).first()
    return user