import uuid
from sqlalchemy import Column, String
from app.api.database import Base 

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()), nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False) 