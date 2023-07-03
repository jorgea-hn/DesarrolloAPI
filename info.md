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

