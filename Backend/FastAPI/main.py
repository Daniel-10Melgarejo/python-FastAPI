from fastapi import FastAPI

app = FastAPI()

#Inicia el server: uvicorn Backend.FastAPI.main:app --reload

@app.get("/")
async def root():
    return "Hello FastAPI"

@app.get("/url")
async def root():
    return {" url_curso" : "http://mouredev.com/python"}