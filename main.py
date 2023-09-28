# from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
# async def read_root(): # Convierte la función en asincrona
    return {"Hello": "World"}

# Define la ruta del recurso
@app.get("/personas")
# Crea una función con el método
def get_personas():
    # Regresa los valores 
    return {"id":1, "nombre": "Patricio"}


@app.get("/v1/contactos")
def get_contactos():
    # TODO read contactos.csv
    # TODO JSON enconde contactos.csv
    # TODO save in response
    datos = []
    with open('contactos.csv', 'r') as file:
        fildnames = ('nombre', 'email')
        lector = csv.DictReader(file, fildnames)
        for row in lector:
            datos.append(row)
    return datos
"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
