from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from api.database import get_db
from api import crud

router = APIRouter(prefix="/api/reports", tags=["Reports"])

@router.get("/top-products")
def top_products(limit: int = Query(10, gt=0), db: Session = Depends(get_db)):
    return crud.get_top_products(db, limit)

@router.get("/visual-content")
def visual_content_stats(db: Session = Depends(get_db)):
    return crud.get_visual_content_stats(db)
