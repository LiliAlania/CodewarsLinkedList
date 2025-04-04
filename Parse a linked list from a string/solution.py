class Node:
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next
def linked_list_from_string(s):
    if s == "None":
        return None
    parts = s.split(" -> ")
    head = Node(int(parts[0]))
    current = head
    for part in parts[1:]:
        if part == "None":
            break
        current.next = Node(int(part))
        current = current.next
    return head
