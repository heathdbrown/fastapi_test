from fastapi import APIRouter

from app.api import crud
from app.api.models import NoteDB, NoteSchema

router = APIRouter()

@router.post("/", response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
            "id": note_id,
            "title": payload.title,
            "description": payload.description,
            }
    return response_object


@router.get("/notes")
async def notes():
    return {"notes": [ {"id": 1, "name": "Note 1", "content": "Note content"}, {"id": 2, "name": "Note 2", "content": "Note content"},] }
