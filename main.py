from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every
from recurring_task import getLatestVideosFromYoutube

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=60)  # 1 hour
def fetchResultsFromYoutube() -> None:
    getLatestVideosFromYoutube()


@app.get("/")
async def fetchVideos():
    return {"message": "Hello World"}
