from flask import Flask

from app.api import get_id, video_list

# Flask app

app = Flask(__name__)
app.config.from_pyfile('../config.py')


# Random tests

# pew = 'pewdiepie'
# tsm = 'talksportmagazine'

# names = list()
# names.append(pew)
# names.append(tsm)

# ids = get_id(pew, tsm)
# v_id = video_list(ids[0], ids[1])
# print(v_id[1])

from app import routes
