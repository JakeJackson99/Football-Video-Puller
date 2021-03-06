import unittest
from app import api

class TestApi(unittest.TestCase):

    # get_id()

    def test_get_id_string(self):
        result = api.get_id('pewdiepie')
        self.assertEqual(result[0], 'UC-lHJZR3Gqxm24_Vd_AJ5Yw')
    
    def test_get_id_string_list(self):
        result = api.get_id('talksportmagazine', 'pewdiepie')
        self.assertEqual(result[0], 'UCWw6scNyopJ0yjMu1SyOEyw')

    def test_get_id_int(self):
        result = api.get_id(1)
        self.assertEqual(result[0], 'UCU8hB4IeMUOc0BS2RApPqFg')
    
    def test_get_id_empty(self):
        result = api.get_id()
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()

