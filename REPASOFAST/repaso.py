from fastapi import FastAPI, HTTPException
from typing import Optional

app= FastAPI(
    title="Mi primer API solita",
    description="María Eugenia Leyva Ávila",
    version="2.0.0"
) 

tareas=[
    {
        "id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI ", "vencimiento": "14-02-25", "estado": "completada"
    },
    {
        "id": 2, "titulo": "Hacer mis tareas", "descripcion": "Realizar mis tareas", "vencimiento": "06-02-25", "estado": "pendiente"
    },
    {
        "id": 3, "titulo": "Terminar mi programa", "descripcion": "Terminar el programa de Fastapi", "vencimiento": "17-02-25", "estado": "pendiente"
    },
    {
        "id": 4, "titulo": "Terminar mi exposición", "descripcion": "Preparar la exposición", "vencimiento": "22-02-25", "estado": "completada"
    }


]

#EndPoint Consultar todas las tareas (GET)
@app.get("/Tareas/", tags=["TAREAS"]) #declarar ruta del servidor
def mostrar(): #funcion que se ejecutará cuando se entre a la ruta
    return {"Tareas registradas: ":tareas} #se muestra la lista de tareas

#EndPoint Consultar tarea específica (GET)
@app.get("/Tareas/{id}", tags=["TAREAS"]) #declarar ruta del servidor
def obtener(id:int): #funcion que se ejecutará cuando se entre a la ruta
    for tarea in tareas:
        if tarea["id"]==id:#si se encuentra la tarea, se le mostrará al usuario
            return tarea
    return {"La tarea no ha sido encontrada"}

#EndPoint crear nueva tarea (POST)
@app.post("/Tareas/", tags=["TAREAS"]) #declarar ruta del servidor
def crear(tareanueva:dict): #funcion que se ejecutará cuando se entre a la ruta
    for tarea in tareas:
        #si la tarea de la peticion ya existe en la bd
        if tarea["id"]==tareanueva.get("id"):
            raise HTTPException(status_code=400, detail="La tarea ya existe") #se mandará este mensaje 
    tareas.append(tareanueva) #si no, se agrega la nueva tarea a la bd
    return(tareanueva)

#EndPoint actualizar tarea (PUT)
@app.put("/Tareas/{id}", tags=["TAREAS"]) #declarar ruta del server 
def actualizar(id:int, tareactualizada:dict): #funcion que se ejecutará cuando se entre a la ruta
    for index, tarea in enumerate(tareas):
        if tarea["id"]==id:
            tareas[index].update(tareactualizada) #se encuentra la tarea solicitada y se actauliza
            return tareas[index]
    raise HTTPException(status_code=404, detail="La tarea no se ha encontrado")


        