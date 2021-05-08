from typing import Optional
from datetime import datetime
from pydantic import BaseModel


class Video(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    thumbnails: dict = None




