from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Json


class Video(BaseModel):
    id: int
    video_id: str
    title: str
    description: Optional[str] = None
    published_at: Optional[datetime] = None
    thumbnails: Optional[Json] = None






