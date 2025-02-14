from fastapi import FastAPI
from typing import Optional

app= FastAPI(
    title="Mi primer API solita",
    description="María Eugenia Leyva Ávila",
    version="2.0.0"
) 

tareas=[
    {
        "id": 1, "titulo": "Estudiar para el examen", "descripcion": "Repasar los apuntes de TAI ", "vencimiento": "14-02-24", "Estado": "completada"
    },
    {
        "id": 2, "titulo": "Hacer mis tareas", "descripcion": "Realizar mis tareas", "vencimiento": "60-02-24", "Estado": "pendiente"
    },
    {
        "id": 3, "titulo": "Terminar mi programa", "descripcion": "Terminar el programa de Fastapi", "vencimiento": "17-02-24", "Estado": "pendiente"
    },
    {
        "id": 4, "titulo": "Terminar mi exposición", "descripcion": "Preparar la exposición", "vencimiento": "22-02-24", "Estado": "completada"
    }


]

#EndPoint Consultar todas las tareas (GET)
@app.get("/Tareas/", tags=["TAREAS"]) #declarar ruta del servidor
def mostrar(): #funcion que se ejecutará cuando se entre a la ruta
    return {"Tareas registradas: ":tareas} #se concatena la lista de tareas