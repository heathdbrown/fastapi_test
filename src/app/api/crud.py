from app.api.models import NoteSchema
from app.db import notes, database

async def post(pyaload: NoteSchema):
    query = notes.insert().values(title=payload.title, description=payload.description)
    return await database.execute(query=query)
