
#  <center>Trabajo Practico N3
##  FastApi
### Por: Darré Juan Cruz
### Universidad Blas Pascal
---
![FastApi](data:image/png;base64,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)


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
