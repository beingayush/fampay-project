from typing import List
import os

import boto3.session
from elasticsearch import Elasticsearch, RequestsHttpConnection
from fastapi import FastAPI, Query
from fastapi_utils.tasks import repeat_every
from requests_aws4auth import AWS4Auth

from app import crud, schemas


from app.recurring_task import get_latest_videos_from_youtube

# Elastic search host url
host = ''
access_key = os.getenv('AWS_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

region = "ap-south-1"
awsauth = AWS4Auth(access_key, secret_key, region, 'es')

es = Elasticsearch(
    hosts=[{'host': host, 'port': 443}],
    http_auth=awsauth,
    use_ssl=True,
    verify_certs=True,
    connection_class=RequestsHttpConnection
)

app = FastAPI()

@app.on_event("startup")
@repeat_every(seconds=60)
def fetchResultsFromYoutube() -> None:
    get_latest_videos_from_youtube()

@app.get("/videos/", response_model=List[schemas.Video])
async def get_videos(skip: int = Query(default=0, ge=0), limit: int = Query(default=25, ge = 0, le=25), query_string: str = ''):
    videos = crud.get_videos(es_client= es, skip=skip, limit=limit, query_string=query_string)
    return videos
