from fastapi import  HTTPException
from typing import  List
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modeloUsuario, modelAuth
from genToken import creartoken
from middleware import BearerJWT
from fastapi.responses import JSONResponse
from DB.conexion import Session, engine, Base
from models.modelsDB import User

from fastapi import APIRouter

routerUsuario=APIRouter()


#EndPoint Consultar Usuarios (GET)
@routerUsuario.get("/todosUsuarios/", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leer(): #funcion que se ejecutará cuando se entre a la ruta
    db=Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible consultar al usuario.", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()


#EndPoint PUT
@routerUsuario.put("/usuarios/{id}", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leeruno(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]= usuarioActualizado.model_dump() #funcion estructura de datos para las vistas
            return usuarios [index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


#endpoint para actualizar a un usuario de la bd
@routerUsuario.put("/Usuario/{id}", tags=["Operaciones CRUD"]) #declar
def actualizarus(id:int, usuario:modeloUsuario):
    db=Session()
    try:
        consulta1=db.query(User).filter(User.id==id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={'mensaje':"Usuario no encontrado"})
        

        consulta1.name=usuario.name
        consulta1.age=usuario.age
        consulta1.email=usuario.email
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario actualizado"})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible actualizar al usuario.", 
                                     "error": str(e)})

#EndPoint Consultar Usuarios por ID (GET)
@routerUsuario.get("/Usuario/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def leeruno(id:int): #funcion que se ejecutará cuando se entre a la ruta
    db=Session()
    try:
        consulta1=db.query(User).filter(User.id==id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={'mensaje':"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta1))
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible consultar al usuario.", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()


#endpoint para eliminar a un usuario de la bd
@routerUsuario.delete("/Usuario/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def eliminarus(id:int):
    db=Session()
    try:
        consulta1=db.query(User).filter(User.id==id).first()
        if not consulta1:
            return JSONResponse(status_code=404, content={'mensaje':"Usuario no encontrado"})
        
        db.delete(consulta1)
        db.commit()
        return JSONResponse(content={"mensaje": "Usuario eliminado"})
    
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "No fue posible eliminar al usuario.", 
                                     "error": str(e)})



#EndPoint POST
@routerUsuario.post("/usuarios/", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
#primero se pide el parametro y luego el tipo de datp que estamos usando
def guardar(usuario:modeloUsuario): #se guarda como usuario diccionario para pedir todos los usuarios juntos
    db=Session() #se crea la sesion
    try:
        db.add(User(**usuario.model_dump())) #se agrega el usuario a la base de datos
        db.commit() #se guarda el usuario
        return JSONResponse(status_code=201,
                            content={"mensaje": "Usuario guardado", ""
                            "usuario": usuario.model_dump()}) #se regresa el mensaje de que se guardó el usuario
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,
                            content={"mensaje": "Error al guardar el usuario", 
                                     "error": str(e)}) #se regresa el mensaje de que hubo un error al guardar el usuario

    finally:
        db.close()

#EndPoint PUT
@routerUsuario.put("/usuarios/{id}", response_model=modeloUsuario, tags=["Operaciones CRUD"]) #declarar ruta del servidor
def actualizar(id:int, usuarioActualizado:modeloUsuario):
    for index, usr in enumerate(usuarios):
        if usr["id"]==id:
            usuarios[index]= usuarioActualizado.model_dump() #funcion estructura de datos para las vistas
            return usuarios [index]
    raise HTTPException(status_code=404, detail="Usuario no encontrado")




#EndPoint DELETE
@routerUsuario.delete("/usuarios/{id}", tags=["Operaciones CRUD"]) #declarar ruta del servidor
def eliminar(id:int, usuarioEliminado:modeloUsuario):
    for index, usr in enumerate (usuarios):
        if usr["id"]==id:
            del usuarios[index] #funcion estructura de datos para las vistas
            return ("El usuario ha sido eliminado.")
        else:
            raise HTTPException(status_code=404, detail="El usuario no se ha encontrado.")
    



