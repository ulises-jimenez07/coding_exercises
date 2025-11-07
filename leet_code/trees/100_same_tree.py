"""
Problem: Check if two binary trees are identical in structure and node values

Approach:
- Recursively compare both trees node by node
- Base case: both None means identical subtrees
- If one is None or values differ, trees aren't same
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) for recursion stack, h is height
"""

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both empty trees are identical
        if p is None and q is None:
            return True

        # One empty, one not
        if p is None or q is None:
            return False

        # Check current nodes and recurse on children
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# --------------------------------------------------------------------------------


class TestIsSameTree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_same_trees(self):
        """Two identical trees."""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(self.solution.isSameTree(p, q))

    def test_different_values(self):
        """Same structure but different values."""
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        q = TreeNode(1, TreeNode(5), TreeNode(3))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_different_structure(self):
        """Different tree structures."""
        p = TreeNode(1, TreeNode(2))
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(self.solution.isSameTree(p, q))

    def test_empty_trees(self):
        """Both trees empty."""
        self.assertTrue(self.solution.isSameTree(None, None))

    def test_one_empty_tree(self):
        """One empty, one non-empty tree."""
        p = TreeNode(1)
        self.assertFalse(self.solution.isSameTree(p, None))
        self.assertFalse(self.solution.isSameTree(None, p))


if __name__ == "__main__":
    unittest.main()
