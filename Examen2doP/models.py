from pydantic import BaseModel, Field

class modeloVehiculo(BaseModel):
    id:int=Field (..., gt=0, description="el ID siempre debe ser positivo")
    año:int=Field (...,ge=1000,le=9999, description="El año debe ser de 4 dígitos")
    modelo:str=Field (..., min_length=4, max_length=25, description="Min 4 caracteres máximo 25")
    placas:str=Field (..., max_length=10, description="Debe tener máximo 10 caracteres")
