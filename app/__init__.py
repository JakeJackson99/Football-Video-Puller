from flask import Flask

from app.api import get_id, video_list

# Flask app
app = Flask(__name__)
app.config.from_pyfile('../config.py')

from app import routes