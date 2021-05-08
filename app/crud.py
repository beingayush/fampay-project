from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Q

from app import schemas


def get_videos(es_client: Elasticsearch, skip: int = 0, limit: int = 25, query_string: str = None):
    s = Search(using=es_client)
    s = s[skip:skip+limit]
    if query_string != '':
        q = Q("multi_match", query=query_string, fields=['title', 'description'])
    else:
        q = Q("match_all")
    response = s.query(q).sort("-published_at")
    videos = []
    for hit in response:
        videos.append(schemas.Video.parse_obj(hit.to_dict()))
    return videos
