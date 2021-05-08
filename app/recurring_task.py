# -*- coding: utf-8 -*-

import os
import uuid
# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
from datetime import datetime, timedelta
from pprint import pprint

import boto3
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

MAX_RESULTS = 50
REQUESTS = 2
# Google api key
API_KEY = ''

dynamo_client = boto3.resource('dynamodb')
# DynamoDb table name to save videos
youtube_table = dynamo_client.Table("Youtube")

def insert_into_dynamo(item: dict):
    try:
        create_video_response = youtube_table.put_item(
            Item= {
                'id': item['id']['videoId'],
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'thumbnails': item['snippet']['thumbnails'],
                'published_at': item['snippet']['publishedAt'],
                'created_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                'updated_at': datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            }
        )
    except Exception as e:
        return




def get_latest_videos_from_youtube():
    try:
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        # credentials = flow.run_console()
        # Get videos published in the last one hour
        youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey= API_KEY)
        last_hour_date_time = (datetime.utcnow() - timedelta(hours=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        request = youtube.search().list(
            part="snippet",
            maxResults=MAX_RESULTS,
            q="cricket",
            order = "date",
            type="video",
            publishedAfter=last_hour_date_time
        )
        count = REQUESTS
        while request is not None and count > 0:
            count -= 1
            response = request.execute()
            pprint(response)
            for item in response['items']:
                insert_into_dynamo(item)
            request = youtube.search().list_next(request, response)
    except Exception as e:
        pass
