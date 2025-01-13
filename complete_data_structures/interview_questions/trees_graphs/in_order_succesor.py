def min_value(node):
    current = node
    while current and current.left:
        current = current.left
    return current


def inOrderSuccessor(root, n):
    if n.right is not None:
        return min_value(n.right)

    p = n.parent
    while p is not None:
        if p.right != n:
            break
        n = p
        p = p.parent
    return p
