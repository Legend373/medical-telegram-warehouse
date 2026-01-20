from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.database import get_db
from api import crud

router = APIRouter(prefix="/api/search", tags=["Search"])

@router.get("/messages")
def search_messages(
    query: str = Query(..., min_length=2),
    limit: int = Query(20, gt=0),
    db: Session = Depends(get_db),
):
    return crud.search_messages(db, query, limit)
