from pydantic import BaseModel
from datetime import date

class SymptomCreate(BaseModel): # form para crear un sintoma
    date: date      # que sea la fecha correcta
    symptom: str    # provisionalmente: que sea texto
    severity: int   # provisionalmente: que sea integrer
    notes: str      # provisionalmente: que sea texto

class SymptomResponse(SymptomCreate):
    id: int

    class Config:
        from_attributes = True # vemos que sea un formato entendible apra pydantic