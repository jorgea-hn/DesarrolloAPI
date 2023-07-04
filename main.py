from typing import List

from fastapi import FastAPI
from fastapi import HTTPException
from database import User
from database import Movie
from database import UserReview
from database import database as connection



from schemas import UserRequestModel
from schemas import UserResponseModel

from schemas import ReviewRequestModel
from schemas import ReviewResponseModel

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

@app.post("/users", response_model=UserResponseModel)
async def create_user(user:UserRequestModel):
    
    if User.select().where(User.username == user.username).exists():
        return HTTPException(409,"El username ya se encuentra en uso")

    hash_password=User.create_password(user.password)
    user = User.create(
        username=user.username,
        password=hash_password
    )

    return user

@app.post("/reviews",response_model=ReviewResponseModel)
async def create_review(user_review:ReviewRequestModel):

    if User.select().where(User.id == user_review.user_id).first() is None:
        raise HTTPException(status_code=404,detail='User not found')
    
    if Movie.select().where(Movie.id == user_review.movie_id).first() is None:
        raise HTTPException(status_code=404,detail='Movie not found')

    user_review = UserReview.create(
        user_id=user_review.user_id,
        movie_id=user_review.movie_id,
        review=user_review.review,
        score=user_review.score
    )

    return user_review

@app.get('/reviews', response_model=List[ReviewResponseModel])
async def get_reviews():
    reviews = UserReview.select() # SELECT * FROM user_reviews:

    return [user_review for user_review in reviews]