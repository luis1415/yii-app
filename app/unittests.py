import unittest
from cube import *

class TestStringMethods(unittest.TestCase):

    def test_create_matrix(self):
        self.assertEqual(create_matrix(2), [[[0, 0], [0, 0]], [[0, 0], [0, 0]]])


    def test_query(self):
        updated = set()
        matrix = create_matrix(2)
        res = exec_command('QUERY 1 1 1 3 3 3', updated, matrix)
        self.assertEqual(res, 0)



if __name__ == '__main__':
    unittest.main()