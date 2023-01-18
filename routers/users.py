import sys

sys.path.append("..")

from fastapi import Depends, HTTPException, APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel
from .auth import get_current_user, get_user_exception, verify_password, get_password_hash


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not Found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/")
async def read_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()

@router.get("/{user_id}")
async def read_user_by_id(user_id: int,
                           db: Session = Depends(get_db)):
    user = db.query(models.Users).\
        filter(models.Users.id == user_id)\
        .first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/user/")
async def read_user_by_id_query(user_id: int,
                           db: Session = Depends(get_db)):
    user = db.query(models.Users).\
        filter(models.Users.id == user_id)\
        .first()
    if user is not None:
        return user
    return 'Invalid User_id'

@router.put("/user/password")
async def user_password_change(user_verification: UserVerification, user: dict = Depends(get_current_user),
                               db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get('id')).first()

    if user is not None:
        if user_verification.username == user_model.username and verify_password(
                user_verification.password
                , user_model.hashed_password):

            user_model.hashed_password = get_password_hash(user_verification.new_password)
            db.add(user_model)
            db.commit()
            return 'Successful'
    return 'Invalid user or request'


@router.delete("/user")
async def delete_user(user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.get("id")).first()

    if user_model is None:
        return "Invalid User"

    db.query(models.Users).filter(models.Users.id == user.get("id")).delete()

    db.commit()

    return 'Delete Successful'
















