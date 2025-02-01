from fastapi import FastAPI
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

#crear segunda ruta o EndPoint
@app.get("/promedio", tags=["Mi calificación TAI"])#declarar ruta del servidor

def promedio(): #funcion que se ejecutará cuando se entre a la ruta
    return 10.5

#crear tercer ruta o endpoint con parametro obligatorio
@app.get("/usuario/{id}", tags=["Parámetro obligatorio"])#declarar ruta del servidor

def consultausuario(id:int): #funcion que se ejecutará cuando se entre a la ruta
    #caso ficticio de consulta a base de datos
    return {"Se encontró el usuario": id}

#crear cuarta ruta o endpoint con parametro opcional
@app.get("/usuario2/", tags=["Parámetro opcional"])#declarar ruta del servidor #se quita el parametro de {}

def consultausuario2(id:Optional[int]=None): #funcion que se ejecutará cuando se entre a la ruta
    if id is not None:#validar si se proporcionó el id
        for usuario in usuarios:#iterar dentro del for
            if usuario["id"]==id:#se verifica si viene el id con el parametro que esta ahi
                return {"mensaje":"usuario encontrado", "El usuario es:":usuario} #mensaje si encuentra el id,usuario
        return {"mensaje":f"No se ha encontrado el id: {id}"} #mensaje si no encuentra el id,usuario
   
    return {"mensaje":"No se proporcionó el id"} #mensaje si no se proporciona el id


#crear cuarto endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
        usuario_id: Optional[int] = None,
        nombre: Optional[str] = None,
        edad: Optional[int] = None
        ):
        
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}