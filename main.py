from fastapi import FastAPI

app = FastAPI(title="Proyecto para reseñar peliculas", descripion="En este proyecto seremos capaces de reseñar peliculas.", version="1")

@app.on_event("startup")
def startup():
    print("El servidor va a comenzar")

@app.on_event("shutdown")
def shutdown():
    print("El servidor se encuentra finalizando")

@app.get("/")
async def index():
    return "Hola mundo, desde servidor en FastAPI"

@app.get("/about")
async def about():
    return "About"

