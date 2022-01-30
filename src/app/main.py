#!/usr/bin/env python3

# Standard Library imports

# Third Party imports
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}
