from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app= FastAPI()
app.title= 'Api Recursos Humanos'

@app.get('/', tags=['inicio'])
def inicio():
    return HTMLResponse('Bienvenido al api de registro')