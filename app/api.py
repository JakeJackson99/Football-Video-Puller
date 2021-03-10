from app import service


def get_id(*username):
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
    except Exception as e:
        print(e)


def video_list(*id_values):
    try:
        if id_values:
            id_list = list()

            for id in id_values:
                    req = service.search().list(
                        part='snippet',
                        channelId=id,
                        maxResults=2,
                        publishedAfter=None,
                        q='a',
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
    except Exception as e:
        print(e)
