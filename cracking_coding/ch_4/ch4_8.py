#get common ancestor for two nodes
from coding_interview.CrackingCoding.ch_4.binary_tree import BinaryTree

#for a node go up until the parent is null, increase a counter for depth
def get_depth(node):
    depth=0
    while node:
        node=node.parent
        depth+=1
    return depth

def first_common_ancestor(p,q):
    if not p or not q:
        return None
    
    #get both nodes depth and compute the delta
    depth_p= get_depth(p)
    depth_q=get_depth(q)
    delta = abs(depth_p-depth_q)
    #move the deepest node up and start from there
    if depth_p < depth_q:
        for _ in range(delta):
            q=q.parent
    else:
        for _ in range(delta):
            p=p.parent
    ancestor_p =p.parent
    ancestor_q= q.parent

    #move up until collision
    while ancestor_p != ancestor_q:
        ancestor_q=ancestor_q.parent
        ancestor_p=ancestor_p.parent
    
    return ancestor_p


t = BinaryTree()
n1 = t.insert(1, None)
n2 = t.insert(2, n1)
n3 = t.insert(3, n1)
n4 = t.insert(4, n2)
n5 = t.insert(5, n2)
n7 = t.insert(7, n3)
n8 = t.insert(8, n4)

ancestor = first_common_ancestor(n3, n4)
print(ancestor.key)