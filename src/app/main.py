#!/usr/bin/env python3

# Standard Library imports

# Third Party imports
from fastapi import FastAPI
from app.api import ping
from app.api import notes

app = FastAPI()

app.include_router(ping.router)
app.include_router(notes.router)
