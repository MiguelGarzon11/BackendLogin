from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from pydantic import BaseModel
from typing import Optional, List

from app.api.database import SessionLocal
from app.api.models.users import User 
from app.api.utils import hash_password

router = APIRouter()

# Esquema de validación con Pydantic
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(
        username = user.username,
        email = user.email,
        password = hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/", response_model=UserCreate)
def login(user: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == user.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found!")

    if user: 
        return User.password
    
    passUser = hash_password(user.password)

    if passUser == User.password:
        raise HTTPException(status_code=200, detail="Login successful")


