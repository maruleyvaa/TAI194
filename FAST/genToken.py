import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from fastapi import HTTPException

def creartoken(data:dict):
    token: str = jwt.encode(payload=data, key="secretkey", algorithm="HS256")#se crea el token
    return token

def validateToken(token:str): #funcion que valida el token
    try:
        data = jwt.decode(token, key="secretkey", algorithms=["HS256"])#se decodifica el token
        return data
    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token expirado")
    except InvalidTokenError:
        raise HTTPException(status_code=403, detail="Token inválido")