def find_node_in_tree(target, root_node):
    if not root_node:
        return False
    if target == root_node:
        return True
    return find_node_in_tree(target, root_node.left) or find_node_in_tree(target, root_node.right)


def find_first_common_ancestor(root_node, n1, n2):
    n1_on_left = find_node_in_tree(n1, root_node.left)
    n2_on_left = find_node_in_tree(n2, root_node.left)

    if n1_on_left ^ n2_on_left:
        return root_node

    if n1_on_left:
        return find_first_common_ancestor(root_node.left, n1, n2)

    return find_first_common_ancestor(root_node.right, n1, n2)
