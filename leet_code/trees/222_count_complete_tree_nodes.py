"""
Problem: Count nodes in a complete binary tree efficiently

Approach:
- Compare left and right subtree depths
- If equal, left is full: count = 2^depth + count(right)
- If different, right is full: count = 2^depth + count(left)
- Time complexity: O(log^2 n) using complete tree properties
- Space complexity: O(log n) for recursion stack
"""

import unittest
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        """Counts the nodes in a complete binary tree efficiently."""
        if not root:
            return 0

        left_depth = self._get_depth(root.left)
        right_depth = self._get_depth(root.right)

        if left_depth == right_depth:
            # Left subtree is a full binary tree.
            return (1 << left_depth) + self.countNodes(root.right)
        else:
            # Right subtree is a full binary tree.
            return (1 << right_depth) + self.countNodes(root.left)

    def _get_depth(self, node: Optional[TreeNode]) -> int:
        """Calculates the depth of the leftmost path of a subtree."""
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth


class TestCountNodes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.countNodes(None), 0)

    def test_single_node(self):
        """Tests a tree with a single node."""
        root = TreeNode(1)
        self.assertEqual(self.solution.countNodes(root), 1)

    def test_complete_tree(self):
        """Tests a complete binary tree that is not full."""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
        self.assertEqual(self.solution.countNodes(root), 6)

    def test_full_tree(self):
        """Tests a full binary tree."""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(self.solution.countNodes(root), 7)


if __name__ == "__main__":
    unittest.main()
