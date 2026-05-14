"""
Problem: Find the diameter (longest path) between any two nodes

Approach:
- Diameter may not pass through root
- Track max path length globally while computing heights
- At each node, diameter = left_height + right_height
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from typing import Optional


class TreeNode:
    """Binary tree node used for diameter calculations."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Computes the diameter of a binary tree."""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_ = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal max_
            if not node:
                return 0

            # Get the max depth of left and right subtrees.
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the maximum diameter passing through this node.
            max_ = max(max_, left + right)

            # Return subtree depth for parent's computation.
            return 1 + max(left, right)

        dfs(root)
        return max_


class TestSolution(unittest.TestCase):
    """Unit tests for diameter-of-binary-tree solution."""

    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: list) -> Optional[TreeNode]:
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

    def test_simple_tree(self):
        """Tests a simple binary tree."""
        root = self.create_tree([1, 2, 3])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 2)

    def test_long_tree(self):
        """Tests a tree with a long path."""
        root = self.create_tree([1, 2, 3, 4, 5, None, None, 6, 7])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 4)

    def test_skewed_tree(self):
        """Tests a skewed tree."""
        root = self.create_tree([1, None, 2, None, 3, None, 4])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 3)

    def test_single_node_tree(self):
        """Tests a tree with only one node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.diameterOfBinaryTree(root), 0)

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.diameterOfBinaryTree(None), 0)


if __name__ == "__main__":
    unittest.main()
