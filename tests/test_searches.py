import unittest
from searches import *


class TestSearchBase(unittest.TestCase):
    arr = list(range(10))

    def setUp(self):
        self.func = binsearch
    
    def test_corners(self):
        # leading corner
        ele = 0
        self.assertEqual(self.func(self.arr, ele), 0)

        # trailing corner
        ele = 9
        self.assertEqual(self.func(self.arr, ele), 9)

    def test_empty(self):
        ele = 5
        self.arr = []
        self.assertEqual(self.func(self.arr, ele), None)

    def test_notfound(self):
        ele = 11
        self.assertEqual(self.func(self.arr, ele), None)

    def test_found(self):
        ele = 5
        self.assertEqual(self.func(self.arr, ele), 5)

        ele = 3
        self.assertEqual(self.func(self.arr, ele), 3)

        ele = 8
        self.assertEqual(self.func(self.arr, ele), 8)


class TestBinarySearch(TestSearchBase):
    def setUp(self):
        self.func = binsearch

# Solution provided by Wojciech B. at https://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class
# Works like magic!
del(TestSearchBase)


if __name__ == '__main__':
    unittest.main()
