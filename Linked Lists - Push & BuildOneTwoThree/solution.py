class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None
def push(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node

def build_one_two_three():
    head = Node(1)
    second = Node(2)
    third = Node(3)
    head.next = second
    second.next = third
