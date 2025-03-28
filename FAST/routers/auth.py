from typing import  List
from modelsPydantic import modeloUsuario, modelAuth
from genToken import creartoken
from middleware import BearerJWT
from fastapi.responses import JSONResponse
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from fastapi import APIRouter


routerAuth=APIRouter()


#endpoint para generar token
@routerAuth.post("/auth", tags=["Autentificación"]) #declarar ruta del servidor
def auth(credenciales:modelAuth): #funcion que se ejecutará cuando se entre a la ruta
    if credenciales.correo=="maru@example.com" and credenciales.passw=="12345678":
        token:str = creartoken(credenciales.model_dump()) #se crea el token con las credenciales
        print(token)
        return JSONResponse(content=token) #se regresa el token
    else:
        return {"Aviso: ": "Credenciales incorrectas"}
    
