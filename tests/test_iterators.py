import unittest
import iterators

class TestBaseIterators(unittest.TestCase):
    def setUp(self):
        pass

    def test_simple(self):
        output = [x for x in iterators.count_to(5)]
        self.assertEqual(output, [0, 1, 2, 3, 4, 5])

    def test_zero(self):
        output = [x for x in iterators.count_to(0)]
        self.assertEqual(output, [0])

    def test_negative(self):
        with self.assertRaises(ValueError): iterators.count_to(-1)


if __name__ == '__main__':
    unittest.main()
