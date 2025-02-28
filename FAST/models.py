from pydantic import BaseModel, Field, EmailStr


class modeloUsuario(BaseModel):
    id:int = Field(..., gt=0, description="Id siempre debe ser positivo")
    nombre:str = Field(..., min_length=1, max_length=85, description="Letras y espacios min. 1,  máx. 85")
    edad:int = Field(..., ge=0, le=105, description="Edad siempre debe ser positiva")
    correo:str = Field(..., pattern="^[\w\.-]+@[\w\.-]+\.\w+$", description="Correo válido")

class modelAuth(BaseModel):
    correo: EmailStr 
    passw: str = Field(..., min_length=8, strip_whitespace=True, description="Contraseña al menos de 8 caracteres")