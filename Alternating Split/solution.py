class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
def alternating_split(head):
    # Your code goes here.
    # Remember to return the context.
    if not head or not head.next:
        raise Exception("List must contain at least two nodes.")
    first_head = head
    second_head = head.next
    first_current = first_head
    second_current = second_head
    current = head.next.next
    is_first_turn = True
    return Context(first_head, second_head)
