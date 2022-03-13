from fastapi import Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, oauth2
from sqlalchemy.orm import Session
from typing import List, Optional
from ..database import  get_db

router = APIRouter(
    prefix= "/users",
    tags=['users']
)
#get all users
@router.get("/", response_model=List[schemas.ResponseUser])
def get_users(db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = "" ):
    # cur.execute("SELECT * FROM users;")
    # records = cur.fetchall()
    result = db.query(models.Users).filter(models.Users.name.contains(search)).limit(limit).offset(skip).all()
    return result

#create user request
@router.post("/",status_code=status.HTTP_201_CREATED, response_model= schemas.ResponseUser)
def add_user(data: schemas.UsersBase, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("INSERT INTO users (name, occupation, age) VALUES ('{0}', '{1}', '{2}') RETURNING *;".format(str(data.name),str(data.occupation),data.age))
    # result=cur.fetchone()
    # conn.commit()
    result = models.Users(login_id=current_user.id, **data.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return result

#get specific user
@router.get("/{id}", response_model= schemas.ResponseUser)
def get_user(id: int, response: Response, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("SELECT * FROM users where id=%s;"%str(id))
    # user=cur.fetchone()
    user = db.query(models.Users).filter(models.Users.id == id).first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    if user.login_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform this action")
    return user    

#delete user
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def del_user(id: int, response: Response, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("DELETE FROM users where id=%s returning *;"%str(id))
    user_query = db.query(models.Users).filter(models.Users.id == id)
    user = user_query.first()
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    if user.login_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform this action")

    user_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#update user
@router.put("/{id}",status_code=status.HTTP_201_CREATED, response_model= schemas.ResponseUser)
def update_user(id:int,users: schemas.UpdateUser, response: Response, db: Session=Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # cur.execute("UPDATE users SET name='{}', occupation='{}', age='{}' where id = '{}' RETURNING *;".format(str(users.name),str(users.occupation),str(users.age), str(id)))
    # result = cur.fetchone()
    # conn.commit()
    user_query = db.query(models.Users).filter(models.Users.id == id)
    user = user_query.first() 
    if user == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found") 
    if user.login_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform this action")
    user_query.update(users.dict(),synchronize_session=False)
    db.commit()
    return user