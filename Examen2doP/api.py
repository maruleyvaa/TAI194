from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
from models import modeloVehiculo


app=FastAPI(
    title="API para gestionar vehículos"

)

vehiculos=[
    {"id":1, "modelo":"Mazda", "año":"2020","placas":"MMM123"},
    {"id":2, "modelo":"Ford", "año":"2018","placas":"AAA321"},
    {"id":3, "modelo":"Chevrolet", "año":"2024","placas":"CCC456"}
]


#endpoint para crear un nuevo vehiculo
@app.post("/vehiculos/", response_model=modeloVehiculo, tags=["Operaciones Vehiculo"])
def guardar(vehiculo:modeloVehiculo):
    for vhl in vehiculos:
        if vhl["id"]==vehiculo.id:
            raise HTTPException(status_code=400, detail="El vehiculo ya existe, ingresa un nuevo ID.")
    vehiculos.append(vehiculo)
    return vehiculo

#endpoint para actualizar vehiculo
@app.put("/vehiculos/{id}", response_model=modeloVehiculo, tags=["Operaciones Vehiculo"])
def actualizar(id:int, vehiculoactualizado:modeloVehiculo):
    for vhl in vehiculos:
        if vhl["id"]==id:
            vhl["modelo"]=vehiculoactualizado.modelo
            vhl["año"]=vehiculoactualizado.año
            vhl["placas"]=vehiculoactualizado.placas
            return vhl
    raise HTTPException(status_code=404, detail="No se encontró el vehículo")
