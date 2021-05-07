# -*- coding: utf-8 -*-

# Sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os
from pprint import pprint

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

MAX_RESULTS = 1
REQUESTS = 1
API_KEY = ''

def getLatestVideosFromYoutube():
    print("Starting job")
    print("Finished job")

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    # credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey= API_KEY)
    request = youtube.search().list(
        part="snippet",
        maxResults=MAX_RESULTS,
        q="surfing",
        type="video"
    )

    count = REQUESTS
    while request is not None and count > 0:
        count -= 1
        response = request.execute()
        print("fetched iteration {}".format(count))
        request = youtube.search().list_next(request, response)