#se importan las librerias necesarias
import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Se crea el nombre de la bd junto con su ubicación
dbName = 'usuarios.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))
dbURL=f"sqlite:///{os.path.join(base_dir, dbName)}"

#crea conexion a la bd
engine= create_engine(dbURL, echo=True)
Session=sessionmaker(bind=engine)
Base= declarative_base()