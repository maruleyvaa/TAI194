import os
from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

dbName = 'usuario.sqlite'
base_dir = os.path.dirname(os.path.abspath(__file__))
dbURL=f"sqlite:///{os.path.join(base_dir, dbName)}"