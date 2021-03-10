
from os import getenv
from flask import Flask
from dotenv import load_dotenv
from googleapiclient.discovery import build


# Flask
app = Flask(__name__)
app.config.from_pyfile('../config.py')

# YouTube API service
load_dotenv()
api_key = getenv('YT_API_KEY', None)
service = build('youtube', 'v3', developerKey=api_key)

# Channel IDs
channel_ids = [
    'UCWw6scNyopJ0yjMu1SyOEyw',     # talkSPORT
    'UCMxNPuhwTVMFkVoRjlARtaQ'      # PewDiePie
]
