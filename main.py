from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

#Endpoints

#Usuarios
@app.get("/usuarios")
async def crear_usuarios():
    #POST
    return {"message": "Hello World"}

@app.get("/usuarios/iniciar_sesion")
async def iniciar_sesion():
    #POST
    return {"message": "Hello World"}

#Tareas