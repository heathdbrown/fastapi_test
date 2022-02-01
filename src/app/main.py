'''main
Main application code
'''
#!/usr/bin/env python3

# Standard Library imports

# Third Party imports
from fastapi import FastAPI
from app.api import notes, ping
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    '''startup
    Connect  to database on startup event
    '''

    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    '''shutdown
    Disconnect from database on shutdown event
    '''

    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
