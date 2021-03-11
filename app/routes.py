# pylint: disable=no-member

# External imports
from flask import render_template, redirect, url_for, session

# Internal imports
from app import app, channel_ids
from app.api import video_list
from app.forms import Keyword


@app.route('/', methods=['GET', 'POST'])
def index():
    """The index page.

    Returns:
        The index page if no keyword has been entered, else it redirects to
        /videos.
    """
    form = Keyword()

    if form.validate_on_submit():
        keyword = form.keyword.data
        session['keyword'] = keyword
        return redirect(url_for('videos'))

    return render_template('index.html', form=form)


@app.route('/videos')
def videos():
    """The videos page.

    Returns:
        The videos page with a list of videos based on videos_ids.
    """
    keyword = session.get('keyword', None)
    video_ids = video_list(*channel_ids, keyword=keyword)
    return render_template('videos.html', video_ids=video_ids)
