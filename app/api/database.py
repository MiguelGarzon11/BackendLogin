# Conexión con el motor (SQLite)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Conexión a SQLite (se guarda en archivo app.db)
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"


# Conectar
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

# Crear sesiones: Puente entre mi código y la base de datos.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 


# Base para modelos
Base = declarative_base()


