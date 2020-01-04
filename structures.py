import random


class Node:
    """
    Unit element
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class SinglyLinkedListStack:
    """
    Where the head of the class is the top of the stack
    """
    head = None

    def __init__(self, head):
        self.head = head

    def push(self, new_head):
        """
        Adds a new element/linked elements to the stack
        """
        cnode = new_head
        while cnode.next:
            cnode = cnode.next

        if self.head:
            cnode.next = self.head

        self.head = new_head

    def pop(self):
        """
        Removes from the top of the stack
        """
        popped = self.head
        self.head = popped.next

        return popped

    def __str__(self):
        res = str(self.head)
        x = self.head

        while x.next:
            res = ', '.join([res, x.next.__str__()])
            x = x.next

        return res


if __name__ == '__main__':
    initstack = SinglyLinkedListStack(None)

    for _ in range(10):
        nd = Node(random.randint(0, 100))
        initstack.push(nd)

    print(initstack)
    print(initstack.pop())
    print(initstack.push(Node(24)))
    print(initstack)