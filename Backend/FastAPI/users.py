from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#Inicia el server: uvicorn Backend.FastAPI.users:app --reload

#entidad user

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int 

users_list = [User(name = "Oscar", surname= "Melgarejo", url = "https://moure.dev",age = 35),
         User(name = "Brais", surname = "Moure", url = "https://moure.dev", age = 35),
         User(name = "Daniel", surname ="Segovia", url = "https://daniel.com", age = 35)]

@app.get("/usersjson")
async def usersjson():
    return [{"name" : "Oscar", "surname" : "Melgarejo", "url" : "https://moure.dev", "age" : 35},
            {"name" : "Brais", "surname" : "Moure", "url" : "https://mouredev.com", "age" : 35},
            {"name" : "Daniel", "surname" : "Segovia", "url" : "https://daniel.com", "age" : 35}]

@app.get("/users")
async def users():
    return users_list
            