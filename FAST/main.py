from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title="Mi primer API",
    description="María Eugenia Leyva Ávila",
    version="1.0.0"
) #mandar al constructor que queremos que tenga este objeto cuando se inicie
#todo se hará a través de este objeto

usuarios=[
    {"id":1, "nombre":"María Eugenia", "edad":"20"},
    {"id":2, "nombre":"Karla", "edad":"22"},
    {"id":3, "nombre":"Ivan", "edad":"25"},
    {"id":4, "nombre":"Estela", "edad":"30"}

]

#crear primera ruta o EndPoint
@app.get("/", tags=["Inicio"])#declarar ruta del servidor
def home(): #funcion que se ejecutará cuando se entre a la ruta
    return {"hello": "world fastApi"}#mensaje que se mostrará en la ruta

    
#EndPoint Consultar Usuarios (GET)
@app.get("/todosUsuarios/", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leer(): #funcion que se ejecutará cuando se entre a la ruta
    return {"Usuarios Registrados: ":usuarios} #se concatena la lista de usuarios

#EndPoint POST
@app.post("/usuarios/", tags=["Operaciones CRUD"]) #declarar ruta del servidor
#primero se pide el parametro y luego el tipo de datp que estamos usando
def guardar(usuario:dict): #se guarda como usuario diccionario para pedir todos los usuarios juntos
    for usr in usuarios:
        #si el usuario de la bd es igual al usuario de la peticion
        if usr["id"]==usuario.get("id"):
            #entonces se mandará el mensaje de error que ya existe
            raise HTTPException(status_code=400, detail="El usuario ya existe") #raise sirve para marcar un punto de quiebre (excepcion) en un ciclo
    

    usuarios.append(usuario) #se agrega el usuario a la lista de usuarios
    return usuario

#EndPoint PUT
@app.put("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def actualizar(id:int, usuarioActualizado:dict):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index].update(usuarioActualizado) #funcion estructura de datos para las vistas
            return usuarios [index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

#EndPoint DELETE
@app.delete("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def eliminar(id:int, usuarioEliminado:dict):
    for index, usr in enumerate (usuarios):
        if usr["id"]==id:
            del usuarios[index] #funcion estructura de datos para las vistas
            return ("El usuario ha sido eliminado.")
        else:
            raise HTTPException(status_code=404, detail="El usuario no se ha encontrado.")
    
