import unittest
from searches import *


class TestSearchBase(unittest.TestCase):
    def setUp(self):
        self.func = binsearch

    def tearDown(self):
        if self.arr:
            del self.arr[:]
    
    def test_corners(self):
        """
        Test head and tail of array
        """
        # leading corner
        ele = 0
        self.assertEqual(self.func(self.arr, ele), 0)

        # trailing corner
        ele = 9
        self.assertEqual(self.func(self.arr, ele), 9)

    def test_empty(self):
        """
        Empty array
        """
        ele = 5
        self.arr = []
        self.assertEqual(self.func(self.arr, ele), None)

    def test_notfound(self):
        """
        Element not in array
        """
        ele = 11
        self.assertEqual(self.func(self.arr, ele), None)

    def test_found(self):
        """
        Basic tests
        """
        ele = 5
        self.assertEqual(self.func(self.arr, ele), 5)

        ele = 3
        self.assertEqual(self.func(self.arr, ele), 3)

        ele = 8
        self.assertEqual(self.func(self.arr, ele), 8)

    def test_single_found(self):
        """
        Single element array
        """
        ele = 0
        self.assertEqual(self.func(self.arr[:1], ele), 0)

    def test_oddarray(self):
        """
        Odd length array
        """
        self.arr += [10]
        print(self.arr)

        ele = 5
        self.assertEqual(self.func(self.arr, ele), 5)

        ele = 8
        self.assertEqual(self.func(self.arr, ele), 8)

        ele = 10
        self.assertEqual(self.func(self.arr, ele), 10)


class TestBinarySearch(TestSearchBase):
    """
    Basic Binary Search
    """
    def setUp(self):
        self.arr = list(range(10))
        self.func = binsearch


class TestRecBinarySearch(TestSearchBase):
    """
    Recursive Binary Search
    """
    def setUp(self):
        self.arr = list(range(10))        
        self.func = rebinsearch

# Solution provided by Wojciech B. at https://stackoverflow.com/questions/1323455/python-unit-test-with-base-and-sub-class
# Works like magic!
del(TestSearchBase)


if __name__ == '__main__':
    unittest.main()
