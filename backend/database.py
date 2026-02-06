import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./medical.db"

# Configurar conexiones entre SQLAlchemy y SQLite3 DB API
engine = create_engine( #motor que nos conecta con sqlite
    DATABASE_URL,
    connect_args={"check_same_thread": False} # para evitar que API tenga mas tarea de la necesaria
)

SessionLocal = sessionmaker(bind=engine) # Conexiones cada vex que abrimos la sesion
Base = declarative_base() # heredan de Base


# Creamos el sintoma -> base detecta el sintoma como tabla -> sessionLocal abrimos un canal de comuniacion -> enginetraduce sintoma a bdd y lo mete a medical.db
