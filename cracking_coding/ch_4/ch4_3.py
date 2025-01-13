from coding_interview.CrackingCoding.ch_2.linked_list import LinkedList
from collections import deque   

class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.name)

def create_node_list_by_depth(tree):
    if not tree:
        return []

    curr = tree
    result = [LinkedList([curr])]
    level = 0

    while result[level]:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            n = linked_list_node.value
            if n.left:
                result[level + 1].add(n.left)
            if n.right:
                result[level + 1].add(n.right)
        level += 1
    return result



node_h = BinaryNode("H")
node_g = BinaryNode("G")
node_f = BinaryNode("F")
node_e = BinaryNode("E", node_g)
node_d = BinaryNode("D", node_h)
node_c = BinaryNode("C", None, node_f)
node_b = BinaryNode("B", node_d, node_e)
node_a = BinaryNode("A", node_b, node_c)

levels=create_node_list_by_depth(node_a)
print(levels[0])
print(levels[1])

result = [LinkedList([node_a])]
[node_a]