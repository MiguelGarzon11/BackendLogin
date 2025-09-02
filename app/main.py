from fastapi import FastAPI
from app.api.database import Base, engine
from app.api.routers import users

# Crear tablas 
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)