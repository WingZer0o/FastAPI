from typing import Union
from fastapi import FastAPI
from routes import hello_world

app = FastAPI()

app.include_router(hello_world.router)