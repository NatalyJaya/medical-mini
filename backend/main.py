from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

import models
import schemas
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#función generadora
def get_db():
    db = SessionLocal() #abrimos peticion
    try:
        yield db # le damos el endpoint solicitado 
    finally:
        db.close() #aseguramos que cerramos la conexion

# CREAMOS SINTOMA
@app.post("/symptoms", response_model=schemas.SymptomResponse)
def create_symptom(symptom: schemas.SymptomCreate, db: Session = Depends(get_db)):
    db_symptom = models.Symptom(**symptom.model_dump()) # esquema pyndantic -> modelo sqlalchemy
    db.add(db_symptom)                                  # registramos la sesion
    db.commit()                                         # confirmamos la transaccion
    db.refresh(db_symptom)                              # refresh datos de la db
    return db_symptom


#OBTENEMOS SINTOMAS -> provisionalmente: listamos
@app.get("/symptoms", response_model=List[schemas.SymptomResponse])
def get_symptoms(db: Session = Depends(get_db)):
    return db.query(models.Symptom).all() #consulta select a través del ORM y devuelve todos los resultados
