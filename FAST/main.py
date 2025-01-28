from fastapi import FastAPI

app= FastAPI() #todo se hará a través de este objeto

#crear primera ruta o EndPoint
@app.get("/")#declarar ruta del servidor

def home(): #funcion que se ejecutará cuando se entre a la ruta
    return {"hello": "world fastApi"}#mensaje que se mostrará en la ruta


