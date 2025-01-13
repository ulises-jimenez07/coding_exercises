from coding_interview.CrackingCoding.ch_4.binary_tree import BinaryTree

def count_sum_paths(tree, target):
    if not isinstance(tree, BinaryTree):
        return None
    return _count_sum_paths(tree.root, target)

def _count_sum_paths(node, target_sum):
    if not node:
        return 0
    return (
        pathsfrom(node, target_sum)
        + _count_sum_paths(node.left, target_sum)
        + _count_sum_paths(node.right, target_sum)
    )

def pathsfrom(node, target_sum):
    if not node:
        return 0
    
    target_sum -= node.key
    counter = 0
    if target_sum == 0:
        counter=+1
    return (
        counter+ pathsfrom(node.left, target_sum)+
        pathsfrom(node.right, target_sum)
    )

t1 = BinaryTree()
n1 = t1.insert(10, None)
n2 = t1.insert(5, n1)
n3 = t1.insert(-3, n1)
n4 = t1.insert(3, n2)
n5 = t1.insert(2, n2)
n6 = t1.insert(3, n4)
n7 = t1.insert(-2, n4)
n8 = t1.insert(1, n5)
n9 = t1.insert(11, n3)
n10 = t1.insert(8, n9)
n11 = t1.insert(-8, n10)

print(count_sum_paths(t1, 8))