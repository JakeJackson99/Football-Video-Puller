from app import service
from datetime import datetime, timedelta


def video_list(*id_values):
    """Creates a list of video IDs that based on the given channel IDs.

    Args:
        *id_values: The ID of a channel.

    Returns:
        A list of video IDs.

     Raises:
        TypeError: An error occuring with a value that cannot be evaluated.
    """
    try:
        if id_values:
            id_list = list()
            date = published_after()

            for id in id_values:
                req = service.search().list(
                    part='snippet',
                    channelId=id,
                    publishedAfter=date,
                    q='city',
                    type='video'
                )
                res = req.execute()
                for video_id in res.get('items'):
                    id_list.append(video_id['id']['videoId'])

            return id_list
        else:
            return None
    except TypeError as e:
        print(e)


def published_after(days=1):
    """Creates the value for 'publishedAfter' for video_list().

    Args:
        days: The number of days ago the return date should be in regard to "now", default=1.

    Returns:
        The the date 24 hours ago in RFC 3339 format.
    """
    date = datetime.utcnow() - timedelta(days=days)
    return date.isoformat('T') + 'Z'


def get_id(*username):
    """Finds a channel's ID based on its username.

    Args:
        *username: The username of a channel.

    Returns: 
        A list of channel IDs.

    Raises:
        TypeError: An error occuring with a value that cannot be evaluated.
    """
    try:
        if username:
            id_list = list()

            for u in username:
                req = service.channels().list(
                    part='id',
                    forUsername=u
                )
                res = req.execute()
                id_list.append(res.get('items')[0]['id'])

            return id_list
        else:
            return None
    except TypeError as e:
        print(e)
