from fastapi import APIRouter

router = APIRouter()


@router.get("/auth")
async def tra():
    return {"asd": 123}
