"""
Problem: Find the maximum path sum in a binary tree

Approach:
- Path can start and end at any nodes
- Use post-order DFS, tracking max gain from each subtree
- At each node, update global max with path through current node
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """Calculates the maximum path sum in a binary tree."""
        # Initialize with a very small number to handle negative node values.
        self.max_sum = -float("inf")

        def find_max_gain(node):
            """Recursively finds the maximum gain from a node downward."""
            if not node:
                return 0

            # Max gain from left and right, ignore paths with negative sums.
            left_gain = max(find_max_gain(node.left), 0)
            right_gain = max(find_max_gain(node.right), 0)

            # Check if the path through the current node is the new maximum.
            current_path_sum = node.val + left_gain + right_gain
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the max gain for a path starting at the current node.
            return node.val + max(left_gain, right_gain)

        find_max_gain(root)
        return int(self.max_sum) if root else 0


class TestMaxPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_complex_tree(self):
        """Tests a tree with a mix of positive and negative values."""
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.maxPathSum(root), 42)

    def test_simple_positive_tree(self):
        """Tests a simple tree with only positive values."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.maxPathSum(root), 6)

    def test_single_negative_node(self):
        """Tests a tree with a single negative node."""
        root = TreeNode(-3)
        self.assertEqual(self.solution.maxPathSum(root), -3)

    def test_single_node(self):
        """Tests a tree with a single node."""
        root = TreeNode(5)
        self.assertEqual(self.solution.maxPathSum(root), 5)

    def test_left_skewed_tree(self):
        """Tests a tree that is skewed to the left."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(4)
        self.assertEqual(self.solution.maxPathSum(root), 10)

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.maxPathSum(None), 0)


if __name__ == "__main__":
    unittest.main()
