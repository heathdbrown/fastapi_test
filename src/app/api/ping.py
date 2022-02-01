"""ping.py
Example fastpi route

"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/ping")
async def pong():
    """ping
    Example function that returns JSON
    """

    return {"ping": "pong!"}
