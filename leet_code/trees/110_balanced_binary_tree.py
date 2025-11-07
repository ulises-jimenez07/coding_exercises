"""
Problem: Check if a binary tree is height-balanced

Approach:
- Use post-order traversal to check balance bottom-up
- Return -1 when subtree is unbalanced for early termination
- Tree is balanced if height difference between subtrees <= 1
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        root_height = self.height(root)
        if root_height == -1:
            return False
        return True

    def height(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1


# ------------------------------------------------------------------------------


class TestIsBalanced(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_balanced_tree(self):
        """Balanced binary tree."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_tree(self):
        """Left-skewed unbalanced tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_single_node_tree(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertTrue(self.solution.isBalanced(root))

    def test_empty_tree(self):
        """Empty tree."""
        root = None
        self.assertTrue(self.solution.isBalanced(root))

    def test_right_skewed_tree(self):
        """Right-skewed unbalanced tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_complex_balanced_tree(self):
        """Complex balanced tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertTrue(self.solution.isBalanced(root))


if __name__ == "__main__":
    unittest.main()
