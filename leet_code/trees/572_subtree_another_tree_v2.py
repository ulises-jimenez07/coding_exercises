"""
Problem: Check if one tree is a subtree of another (alternative approach)

Approach:
- Same as v1: helper function for tree identity check
- Recursively check if subRoot matches at any position
- Time complexity: O(m * n) where m, n are node counts
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from typing import (
    List,
    Optional,
)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_identical(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
    # Both nodes are None, they are identical.
    if not node1 and not node2:
        return True
    # One node is None or values differ, they are not identical.
    if not node1 or not node2 or node1.val != node2.val:
        return False
    # Recursively check left and right children.
    return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # An empty subRoot is always a subtree.
        if not subRoot:
            return True
        # If root is empty but subRoot is not, it cannot be a subtree.
        if not root:
            return False
        # Check if current trees are identical.
        if is_identical(root, subRoot):
            return True
        # Recursively check left and right subtrees of root.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


class TestIsSubtree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return root

    def test_is_subtree(self):
        """Tests if a tree is a subtree of another."""
        root = self.create_tree([3, 4, 5, 1, 2])
        subRoot = self.create_tree([4, 1, 2])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_is_not_subtree(self):
        """Tests if a tree is not a subtree of another."""
        root = self.create_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = self.create_tree([4, 1, 2])
        self.assertFalse(self.solution.isSubtree(root, subRoot))

    def test_identical_trees(self):
        """Tests if two identical trees are subtrees of each other."""
        root = self.create_tree([1, 2, 3])
        subRoot = self.create_tree([1, 2, 3])
        self.assertTrue(self.solution.isSubtree(root, subRoot))

    def test_empty_subtree(self):
        """Tests if an empty tree is a subtree of another tree."""
        root = self.create_tree([1, 2, 3])
        self.assertTrue(self.solution.isSubtree(root, None))

    def test_empty_tree(self):
        """Tests if a tree is a subtree of an empty tree."""
        subRoot = self.create_tree([1, 2, 3])
        self.assertFalse(self.solution.isSubtree(None, subRoot))


if __name__ == "__main__":
    unittest.main()
