# from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

# Define la ruta del recurso
@app.get("/personas")
# Crea una función con el método
def get_personas():
    # Regresa los valores 
    return {"id":1, "nombre": "Patricio"}

"""
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
"""
