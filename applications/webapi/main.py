from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/version")
def version():
    return "1.0.0"
