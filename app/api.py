from googleapiclient.discovery import build
from os import getenv
from dotenv import load_dotenv

# YouTube API service
load_dotenv()
api_key = getenv('YT_API_KEY', None)
service = build('youtube', 'v3', developerKey=api_key)


def get_id(*username):
    if username:
        id_list = list()

        for u in username:
            req = service.  channels().list(
                part='id',
                forUsername=u
            )
            res = req.execute()
            id_list.append(res.get('items')[0]['id'])

        return id_list
    else:
        return None


def video_list(*id_values):
    if all(i is not str for i in id_values):
        return None
    
    if id_values:
        id_list = list()

        for i in id_values:
            req = service.search().list(
                part='snippet',
                channelId=i,
                maxResults=1,
                publishedAfter=None,
                q='city',
                type='video'
            )
            res = req.execute()
            id_list.append(res.get('items')[0]['id']['videoId'])

        return id_list
    else:
        return None
