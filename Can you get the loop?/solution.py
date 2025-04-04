def loop_size(node):
    slow, fast = node, node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return 0
    count = 1
    fast = fast.next
    while slow != fast:
        fast = fast.next
        count += 1
    return count
