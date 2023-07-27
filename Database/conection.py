from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

#para usar variables de entonrno
from dotenv import load_dotenv
import os

from sqlalchemy.ext.declarative import declarative_base

#load_dotenv(dotenv_path=None)

conexion_bd = os.getenv('ConexionBD')

motor= create_engine(conexion_bd, echo=True)

session = sessionmaker(bind=motor)

base = declarative_base()