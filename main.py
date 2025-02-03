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
@app.get("/usuarios/iniciar_sesion/{id}/tareas")
async def get_tareas_list_user():
    #GET (?)
    return {"message": "Hello World"}

#POST? aquí que se hace?
@app.get("/POST/tareas")
async def crear_tarea():
    #POST
    return {"message": "Hello World"}

@app.get("PUT/tareas/{id}")
async def actualizar_tarea():
    #PUT
    return {"message": "Hello World"}

@app.get("DELETE/tareas/{id}")
async def actualizar_tarea():
    #DELETE
    return {"message": "Hello World"}

@app.get("GET/tareas/{id}")
async def get_tarea_por_ID():
    #GET
    return {"message": "Hello World"}


#Categorias
@app.get("/POST/categorias")
async def crear_categoria():
    #POST
    return {"message": "Hello World"}

@app.get("/DELETE/categorias/{id}")
async def eliminar_categoria():
    #DELETE
    return {"message": "Hello World"}

@app.get("/GET/categorias")
async def get_categoria():
    #GET
    return {"message": "Hello World"}
