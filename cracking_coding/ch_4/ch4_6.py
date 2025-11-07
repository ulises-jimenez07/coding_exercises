# find next node of a given node in a binary search tree
from coding_interview.CrackingCoding.ch_4.binary_search_tree import BinarySearchTree


def in_order_successor(input_node):
    if input_node is None:
        return None

    # if node has right subtree we get the leftmost child
    if input_node.right:
        current = input_node.right
        while current.left:
            current = current.left
        return current

    # if not we need to go up to the parent
    # until the child is not rigth child, that means until is not greater
    # than its parent
    ancestor = input_node.parent
    child = input_node

    while ancestor and ancestor.right == child:
        child = ancestor
        ancestor = ancestor.parent

    return ancestor


bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

# Test all nodes
inputs = [5, 9, 11, 12, 14, 20, 25]
outputs = inputs[1:]
outputs.append(None)

for x, y in zip(inputs, outputs):
    test = bst.get_node(x)
    succ = in_order_successor(test)
    if succ is not None:
        print(succ.key)
    else:
        print(succ)
