# Creacion de una API

## Creacion de entorno virtual
python -m venv entorno
entorno\Scripts\ctivate

## Instalacion de FastAPI y uvicorn 
pip install fastapi
pip install uvicorn

## Correr el servidor
uvicorn main:app --reload


## Documentacion
Cuando trabajas con FastAPI se crea la documentacion automaticamente
http://localhost:8000/docs

## Eventos
Se deben colocar decoradores para que se ejecuten los eventos

@app.on_event("startup") Para que se ejecute al iniciar
def startup():
    print("El servidor va a comenzar")


@app.on_event("shutdown")  Para que se ejecute al final 
def shutdown():
    print("El servidor se encuentra finalizando")


## Conexion a bases de datos
Esta es una ORM y permite interactuar con la base de datos
pip install peewee 

Para conectarnos con el gestor
pip install mysqlclient

Entramos a la base de datos mysql
mysql -u root -p
colocamos la contraseña

creamos la base de datos
CREATE DATABASE fastapi

miramos si hay tablas
SHOW TABLES;

Para ver las tablas
DESC users;
