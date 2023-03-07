from fastapi import APIRouter

router = APIRouter()


@router.get("/ads")
async def tra():
    return {"asd": 123}
