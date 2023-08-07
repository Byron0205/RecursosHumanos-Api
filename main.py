from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse

from fastapi.encoders import jsonable_encoder

#importaciones para bd
from Database.conection import session,base, motor
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

#solucionar problemas de cors
from fastapi.middleware.cors import CORSMiddleware

#importar modelos
from models.Persona import personas 

app= FastAPI()
app.title= 'Api Recursos Humanos'


#configuracion del cors
origins = [
    "http://localhost",
    "http://localhost:5000",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://ti-usr3-cp.cuc-carrera-ti.ac.cr",
    "https://ti-usr3-cp.cuc-carrera-ti.ac.cr/registro/1",
    "https://ti-usr3-cp.cuc-carrera-ti.ac.cr/registro/2",
    "https://dragonic.netlify.app/"
]

# Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


#inicializacion de bd
base.metadata.create_all(bind=motor)

@app.get('/', tags=['inicio'])
def inicio():
    return HTMLResponse('Bienvenido al api de registro')


@app.get('/personas', tags=['personas'])
def getPersonas():
    bd =session()

    result = bd.query(personas).all()

    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@app.get('/persona', tags=['personas'])
def getPersona(id:int):
    bd= session()

    result = bd.query(personas).filter(personas.ID == id).first()

    return JSONResponse(content=jsonable_encoder(result), status_code=200)