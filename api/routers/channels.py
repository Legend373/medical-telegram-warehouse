from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.database import get_db
from api import crud

router = APIRouter(prefix="/api/channels", tags=["Channels"])

@router.get("/{channel_name}/activity")
def channel_activity(channel_name: str, db: Session = Depends(get_db)):
    return crud.get_channel_activity(db, channel_name)
