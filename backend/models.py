from sqlalchemy import Column, Integer, String, Date
from database import Base

class Symptom(Base): # MODELO DE LA BASE DE DATOS
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    symptom = Column(String, index=True)
    severity = Column(Integer)
    notes = Column(String)