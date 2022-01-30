#!/usr/bin/env python3

# Standard Library imports

# Third Party imports
from fastapi import FastAPI
from app.api import ping

app = FastAPI()

app.include_router(ping.router)
