"""
Problem: Find the maximum depth of a binary tree

Approach:
- Use recursion to find depth of left and right subtrees
- Maximum depth is 1 + max(left_depth, right_depth)
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth_left = self.maxDepth(root.left)
        depth_right = self.maxDepth(root.right)

        return 1 + max(depth_left, depth_right)


class TestMaxDepth(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Empty tree."""
        self.assertEqual(self.solution.maxDepth(None), 0)

    def test_single_node(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.maxDepth(root), 1)

    def test_balanced_tree(self):
        """Balanced tree."""
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        self.assertEqual(self.solution.maxDepth(root), 3)

    def test_left_skewed_tree(self):
        """Left-skewed tree."""
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        self.assertEqual(self.solution.maxDepth(root), 4)

    def test_right_skewed_tree(self):
        """Right-skewed tree."""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.assertEqual(self.solution.maxDepth(root), 4)


if __name__ == "__main__":
    unittest.main()
