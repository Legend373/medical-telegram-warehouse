from pydantic import BaseModel
from typing import List, Optional

class TopProduct(BaseModel):
    term: str
    count: int

class ChannelActivity(BaseModel):
    channel_name: str
    message_date: str
    message_count: int

class MessageSearchResult(BaseModel):
    message_id: int
    channel_name: str
    message_date: str
    text: str

class VisualContentStats(BaseModel):
    channel_name: str
    image_category: str
    image_count: int
