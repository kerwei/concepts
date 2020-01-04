import unittest

from structures import Node, SinglyLinkedListStack


class TestSinglyLinkedListStack(unittest.TestCase):
    def setUp(self):
        self.teststack = SinglyLinkedListStack(None)

        for i in [1, 2, 3, 4, 5]:
            self.teststack.push(Node(i))

    def testPush(self):
        """
        Test that push always places an element at the top of th stack
        """
        self.teststack.push(Node(10))
        self.assertSequenceEqual(self.teststack.__str__(), '10, 5, 4, 3, 2, 1')

    def testPop(self):
        """
        Test that pop always remove an element from the top of the stack
        """
        self.assertEqual(self.teststack.pop().__str__(), '5')
