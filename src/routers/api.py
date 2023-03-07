from fastapi import APIRouter

# from . import auth, consumers, sellers, ads
from . import ads
from ..config import ROUTE_PREFIX_V1

router = APIRouter()


def include_api_routes():
    # router.include_router(auth.router)
    router.include_router(ads.router, prefix=ROUTE_PREFIX_V1)
    # router.include_router(consumers.router, prefix=ROUTE_PREFIX_V1)
    # router.include_router(sellers.router, prefix=ROUTE_PREFIX_V1)


include_api_routes()
