from fastapi import FastAPI
from app.api.database import Base, engine
from app.api.routers import users
from fastapi.middleware.cors import CORSMiddleware

# Crear tablas 
Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(users.router)