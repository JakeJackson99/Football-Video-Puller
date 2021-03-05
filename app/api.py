import os

from googleapiclient.discovery import build

# YouTube API service
api_key = os.environ['YT_API_KEY']
service = build('youtube', 'v3', developerKey=api_key)


def get_id(username):
    req = service.channels().list(
        part='id',
        forUsername=username
    )

    res = req.execute()
    return res.get('items')[0]['id']


def video_list(id, q):
    req = service.search().list(
        part = 'snippet',
        channelId = id,
        maxResults = 1,
        publishedAfter = None,
        q = q,
        type = 'video'
    )

    res = req.execute()

    video_id = res.get('items')[0]['id']['videoId']

    return video_id

