# Validate BST


class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def min_value(root):
    if root is None:
        return float("inf")
    return min(root.val, min_value(root.left), min_value(root.right))


def max_value(root):
    if root is None:
        return float("-inf")
    return max(root.val, max_value(root.left), max_value(root.right))


def isValidBST_2(root):
    if root is None:
        return True
    if root.right and root.val > max_value(root.right):
        return False
    if root.left and root.val < max_value(root.left):
        return False
    return isValidBST(root.left) and isValidBST(root.right)


def isValidBST(root):
    def _is_valid_bst(root, min_val=float("-inf"), max_val=float("inf")):
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False

        return _is_valid_bst(root.left, min_val, root.val) and _is_valid_bst(
            root.right, root.val, max_val
        )

    return _is_valid_bst(root)
