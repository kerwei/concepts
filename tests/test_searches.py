import unittest
from searches import *

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.arr = list(range(10))

    def test_corners(self):
        # leading corner
        ele = 0
        self.assertEqual(binsearch(self.arr, ele), 0)

        # trailing corner
        ele = 9
        self.assertEqual(binsearch(self.arr, ele), 9)

    def test_empty(self):
        ele = 5
        self.arr = []
        self.assertEqual(binsearch(self.arr, ele), None)

    def test_notfound(self):
        ele = 11
        self.assertEqual(binsearch(self.arr, ele), None)

    def test_found(self):
        ele = 5
        self.assertEqual(binsearch(self.arr, ele), 5)

        ele = 3
        self.assertEqual(binsearch(self.arr, ele), 3)

        ele = 8
        self.assertEqual(binsearch(self.arr, ele), 8)