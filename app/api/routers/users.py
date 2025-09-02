from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.api.database import SessionLocal
from app.api.models.users import User 
from app.api.utils import hash_password

router = APIRouter()

# Esquema de validación con Pydantic
class UserCreate(BaseModel):
    username: str
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

