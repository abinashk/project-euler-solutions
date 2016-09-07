class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None

class LinkedList:
    def __init__(self, node=None):
        self.head = node

    def flatten(self):
        node = self.head
        while node is not None:
            next = node.next
            if node.child:
                node.next = node.child
