from fastapi import FastAPI, HTTPException, Depends
from typing import  List
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modeloUsuario, modelAuth
from genToken import creartoken
from middleware import BearerJWT
from fastapi.responses import JSONResponse
from DB.conexion import Session, engine, Base
from models.modelsDB import User
from routers.usuarios import routerUsuario
from routers.auth import routerAuth




app= FastAPI(
    title="Mi primer API",
    description="María Eugenia Leyva Ávila",
    version="1.0.0"
) #mandar al constructor que queremos que tenga este objeto cuando se inicie
#todo se hará a través de este objeto


Base.metadata.create_all(bind=engine)


#crear primera ruta o EndPoint
@app.get("/", tags=["Inicio"])#declarar ruta del servidor
def home(): #funcion que se ejecutará cuando se entre a la ruta
    return {"hello": "world fastApi"}#mensaje que se mostrará en la ruta


app.include_router(routerUsuario) #se incluye el router de usuarios
app.include_router(routerAuth) #se incluye el router de autentificacion


