from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def base_admin_route():
    """

    :return:
    """
    return {"message": "Admin getting schwifty"}
