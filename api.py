from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from graficos import graficos


app = FastAPI()
app.mount("/static",StaticFiles(directory="static/"),name="static")



 
app.include_router(graficos)