from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import  get_db

router = APIRouter(
    prefix= "/accounts",
    tags=['accounts']
)

@router.get("/{id}", response_model=schemas.Userout)
def get_accounts(id: int, db: Session=Depends(get_db)):
    user = db.query(models.Login).filter(models.Login.id == id).first()
    if not user:
        HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user

@router.post("/signup",status_code=status.HTTP_201_CREATED, response_model=schemas.Userout)
def create_user(user: schemas.Signup, db: Session=Depends(get_db)):
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.Login(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

