from fastapi import APIRouter

router = APIRouter()


@router.get("/sellers")
async def tra():
    return {"asd": 123}
