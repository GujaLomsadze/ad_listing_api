from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from ..dependencies import get_token_header, get_db

from ..domain.ad import service

router = APIRouter(
    prefix="/ads",
    tags=["Advertisements"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)


@router.get("/fetch_ads/")
def read_ads(start_from: int = 0, limit: int = 100, db=Depends(get_db)):
    ads = service.get_ads(db=db, start_from=start_from, limit=limit)

    items = {"data": ads}
    return items
