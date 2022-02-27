from email import message
from fastapi import status, HTTPException, Depends, APIRouter, Response
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(tags=['Authentication'])

@router.post('/login')
def login(user_credentials: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.Login).filter(models.Login.email == user_credentials.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid crendentials")

    if not utils.hash_verify(user_credentials.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"invalid crendentials")
    
    return {"token":"get_success"}