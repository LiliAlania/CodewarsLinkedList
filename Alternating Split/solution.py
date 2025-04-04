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
    while current:
        if is_first_turn:
            first_current.next = current
            first_current = first_current.next
        else:
            second_current.next = current
            second_current = second_current.next
        is_first_turn = not is_first_turn
        current = current.next
    first_current.next = None
    second_current.next = None
    return Context(first_head, second_head)
