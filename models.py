import datetime
from sqlalchemy import Column, Integer, String, DateTime, JSON
from .database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(String)
    published_at = Column(DateTime)
    thumbnails = Column(JSON)

    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    class Config:
        orm_mode = True