from fastapi import FastAPI, HTTPException, Depends
from typing import  List
from pydantic import BaseModel
from models import modeloUsuario, modelAuth
from genToken import creartoken
from middleware import BearerJWT
from fastapi.responses import JSONResponse


app= FastAPI(
    title="Mi primer API",
    description="María Eugenia Leyva Ávila",
    version="1.0.0"
) #mandar al constructor que queremos que tenga este objeto cuando se inicie
#todo se hará a través de este objeto


usuarios=[
    {"id":1, "nombre":"María Eugenia", "edad":"20","correo":"maru@example.com"},
    {"id":2, "nombre":"Karla", "edad":"22","correo":"karla@example.com"},
    {"id":3, "nombre":"Ivan", "edad":"25","correo":"ivan@example.com"},
    {"id":4, "nombre":"Estela", "edad":"30","correo":"estela@example.com"}

]

#crear primera ruta o EndPoint
@app.get("/", tags=["Inicio"])#declarar ruta del servidor
def home(): #funcion que se ejecutará cuando se entre a la ruta
    return {"hello": "world fastApi"}#mensaje que se mostrará en la ruta



#endpoint para generar token
@app.post("/auth", tags=["Autentificación"]) #declarar ruta del servidor
def auth(credenciales:modelAuth): #funcion que se ejecutará cuando se entre a la ruta
    if credenciales.correo=="maru@example.com" and credenciales.passw=="12345678":
        token:str = creartoken(credenciales.model_dump()) #se crea el token con las credenciales
        print(token)
        return JSONResponse(content=token) #se regresa el token
    else:
        return {"Aviso: ": "Credenciales incorrectas"}

    
#EndPoint Consultar Usuarios (GET)
@app.get("/todosUsuarios/", tags=["Operaciones CRUD"], dependencies=[Depends(BearerJWT())], response_model=List[modeloUsuario]) #declarar ruta del servidor
def leer(): #funcion que se ejecutará cuando se entre a la ruta
    return usuarios

#EndPoint POST
@app.post("/usuarios/", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
#primero se pide el parametro y luego el tipo de datp que estamos usando
def guardar(usuario:modeloUsuario): #se guarda como usuario diccionario para pedir todos los usuarios juntos
    for usr in usuarios:
        #si el usuario de la bd es igual al usuario de la peticion
        if usr["id"]==usuario.id:
            #entonces se mandará el mensaje de error que ya existe
            raise HTTPException(status_code=400, detail="El usuario ya existe") #raise sirve para marcar un punto de quiebre (excepcion) en un ciclo
    

    usuarios.append(usuario) #se agrega el usuario a la lista de usuarios
    return usuario

#EndPoint PUT
@app.put("/usuarios/{id}", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
def actualizar(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]= usuarioActualizado.model_dump() #funcion estructura de datos para las vistas
            return usuarios [index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#EndPoint DELETE
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def eliminar(id:int, usuarioEliminado:modeloUsuario):
    for index, usr in enumerate (usuarios):
        if usr["id"]==id:
            del usuarios[index] #funcion estructura de datos para las vistas
            return ("El usuario ha sido eliminado.")
        else:
            raise HTTPException(status_code=404, detail="El usuario no se ha encontrado.")
    



