from Database.conection import base
from sqlalchemy import Column, Integer, String

class personas(base):
    __tablename__= 'personas'
    
    ID= Column(Integer, primary_key=True)
    Nombre = Column(String(length= 50))
    last_name = Column(String(length= 50))
    Sexo = Column(String(length=1))


