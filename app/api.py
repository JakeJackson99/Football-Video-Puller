from googleapiclient.discovery import build
import os

# YouTube API service
api_key = os.environ['YT_API_KEY']
service = build('youtube', 'v3', developerKey=api_key)

def get_id(username):
    req = service.channels().list(
        part='id',
        forUsername=username
    )

    res = req.execute()
    return res['items'][0]['id']
    

def get_video_id():
    pass