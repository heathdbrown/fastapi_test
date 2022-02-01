'''models.py
Uses pydantic to model data

'''

from pydantic import BaseModel


class NoteSchema(BaseModel):
    '''NoteSchema
    Models Note entry
    '''
    title: str
    description: str


class NoteDB(NoteSchema):
    '''NotDB
    Models data for database entries
    '''
    id: int
