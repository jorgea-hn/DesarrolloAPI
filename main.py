from fastapi import FastAPI
from database import User
from database import Movie
from database import UserReview
from database import database as connection

from schemas import UserBaseModel

app = FastAPI(title="Proyecto para reseñar peliculas", descripion="En este proyecto seremos capaces de reseñar peliculas.", version="1")

@app.on_event("startup")
def startup():
    # print("El servidor va a comenzar")
    if connection.is_closed():
        connection.connect()
        print("Connecting...")
    
    connection.create_tables([User,Movie,UserReview])

@app.on_event("shutdown")
def shutdown():
    # print("El servidor se encuentra finalizando")
    if not connection.is_closed():
        connection.close()
        print("Close")

@app.get("/")
async def index():
    return "Hola mundo, desde servidor en FastAPI"

@app.get("/about")
async def about():
    return "About"

@app.post("/users")
async def create_user(user:UserBaseModel):
     
    user = User.create(
        username=user.username,
        password=user.password
    )

    return user.id

