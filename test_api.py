import unittest
from app import api

"""TODO:
- test video_list() with 'id[0], id[1]' to fail
- change return strings as they change per day
"""


class TestApi(unittest.TestCase):

    # get_id()

    def test_get_id_string(self):
        result = api.get_id('pewdiepie')
        self.assertEqual(result[0], 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')

    def test_get_id_string_multiple_args1(self):
        result = api.get_id('talksportmagazine', 'pewdiepie')
        self.assertEqual(result[0], 'UCWw6scNyopJ0yjMu1SyOEyw')

    def test_get_id_string_multiple_args2(self):
        result = api.get_id('talksportmagazine', 'pewdiepie')
        self.assertEqual(result[1], 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')

    def test_get_id_int(self):
        result = api.get_id(1)
        self.assertEqual(result[0], 'UCU8hB4IeMUOc0BS2RApPqFg')

    def test_get_id_empty(self):
        result = api.get_id()
        self.assertEqual(result, None)

    # video_list()

    def test_video_list_string(self):
        id = api.get_id('talksportmagazine')
        result = api.video_list(*id)
        self.assertEqual(result[0], '-C1as8I-qhg')

    def test_video_list_string_multiple_args1(self):
        id = api.get_id('talksportmagazine', 'pewdiepie')
        result = api.video_list(*id)
        self.assertEqual(result[0], '-C1as8I-qhg')

    def test_video_list_string_multiple_args2(self):
        id = api.get_id('talksportmagazine', 'pewdiepie')
        result = api.video_list(*id)
        self.assertEqual(result[1], 'oLAw5EGe1zY')

    def test_video_list_int(self):
        result = api.video_list(1)
        self.assertEqual(result, None)

    def test_video_list_empty(self):
        result = api.video_list()
        self.assertEqual(result, None)

    def test_video_list_no_keyword(self):
        id = api.get_id('talksportmagazine')
        result = api.video_list(*id, 'city')
        self.assertEqual(result[0], 'dunnoyet')


if __name__ == "__main__":
    unittest.main()
