from fastapi import APIRouter

router = APIRouter()


@router.get("/def")
async def tra():
    return {"asd": 123}
