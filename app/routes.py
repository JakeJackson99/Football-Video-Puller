from flask import render_template

from app import app, channel_ids
from app.api import video_list


@app.route('/')
def index():
    video_ids = video_list(*channel_ids)
    return render_template('index.html', video_ids=video_ids)
