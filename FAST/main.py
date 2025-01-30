from fastapi import FastAPI

app= FastAPI() #todo se hará a través de este objeto

#crear primera ruta o EndPoint
@app.get("/")#declarar ruta del servidor

def home(): #funcion que se ejecutará cuando se entre a la ruta
    return {"hello": "world fastApi"}#mensaje que se mostrará en la ruta

#crear segunda ruta o EndPoint
@app.get("/promedio")#declarar ruta del servidor

def promedio(): #funcion que se ejecutará cuando se entre a la ruta
    return 10.5

#crear tercer ruta o endpoint con parametro obligatorio
@app.get("/usuario/{id}")#declarar ruta del servidor

def consultausuario(id:int): #funcion que se ejecutará cuando se entre a la ruta
    #caso ficticio de consulta a base de datos
    return {"Se encontró el usuario": id}
