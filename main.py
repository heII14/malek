from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/ping")
async def pong():
    return {"message": "pong"}

@app.get("/sum")
async def sum(a: Optional[int] = None, b: Optional[int]= None):
    if a and b:
        return {"result": a+b}