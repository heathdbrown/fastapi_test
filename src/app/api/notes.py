from fastapi import APIRouter

router = APIRouter()

@router.get("/notes")
async def notes():
    return {"notes": [ {"id": 1, "name": "Note 1", "content": "Note content"}, {"id": 2, "name": "Note 2", "content": "Note content"},] }
