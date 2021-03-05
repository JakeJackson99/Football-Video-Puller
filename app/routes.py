from flask import render_template

from app import app
from app.api import get_id, video_list

"""
Channel usernames:
- talkSPORTmagazine
"""


@app.route('/')
def index():
    id = get_id('talksportmagazine')
    video_id = video_list(id, 'city')
    return render_template('index.html', video_id=video_id)
