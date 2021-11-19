
#  <center>Trabajo Practico N3
##  FastApi
### Por: Darré Juan Cruz
### Universidad Blas Pascal
---
![enter image description here](https://repository-images.githubusercontent.com/160919119/29516980-f308-11e9-9096-0836920fdae3)


## Información básica para poder entender el proyecto

 - [Python (Wikipedia)](https://es.wikipedia.org/wiki/Python "Python") 
 - [Python](https://www.python.org)
 - [FastApi](https://fastapi.tiangolo.com) 
 

# <center> ¿Qué es FastApi?

>FastAPI es un web framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.6+ basado en las anotaciones de tipos estándar de Python.
---
## Instalar FastApi

 

    $ pip install fastapi[all]

## Código simple en FastApi

    from fastapi import FastAPI
    
    app = FastAPI()
    
    
    @app.get("/")
    async def root():
        return {"message": "Hello World"}
El siguiente código devuelve un mensaje de Hello World

Nota :
El comando  `uvicorn main:app`  se refiere a:

-   `main`: el archivo  `main.py`  (el "módulo" de Python).
-   `app`: el objeto creado dentro de  `main.py`  con la línea  `app = FastAPI()`.
-   `--reload`: hace que el servidor se reinicie cada vez que cambia el código. Úsalo únicamente para desarrollo.
