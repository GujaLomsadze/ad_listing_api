from fastapi import APIRouter

router = APIRouter()


@router.get("/consumers")
async def tra():
    return {"asd": 123}
