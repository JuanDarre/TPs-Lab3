from fastapi import FastAPI

app = FastAPI(  Title="Titulo del proyecto",
                description="Programa introductorio a FastAPI",
                version="1.0.0")

@app.get("/")
def index():
    return "Hola Mundo"

@app.get("/about") 
def about():
    return "Estamos en el about"   