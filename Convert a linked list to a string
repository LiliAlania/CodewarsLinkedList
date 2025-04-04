class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
def stringify(node):
    res = ''
    cur_node = node
    while cur_node is not None:
        res += f'{cur_node.data}'
        res += ' -> '
        cur_node = cur_node.next
    res += 'None'
    return res
