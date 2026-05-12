"""Problem: compute the total tilt of a binary tree."""

import unittest
from typing import Optional


class TreeNode:
    """Binary tree node used in tests."""

    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """DFS solution for total tree tilt."""

    def findTilt(self, root: Optional[TreeNode]) -> int:
        total_tilt = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal total_tilt
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Each node contributes the absolute difference of subtree sums.
            total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        dfs(root)
        return total_tilt


class TestFindTilt(unittest.TestCase):
    """Unit tests for findTilt."""

    def test_example_tree(self):
        """Balanced example with known tilt."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(Solution().findTilt(root), 1)

    def test_larger_tree(self):
        """Tree with multiple levels and cumulative tilt."""
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(9)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(7)

        self.assertEqual(Solution().findTilt(root), 15)

    def test_single_node(self):
        """Single node has zero tilt."""
        root = TreeNode(42)
        self.assertEqual(Solution().findTilt(root), 0)

    def test_empty_tree(self):
        """Empty tree has zero tilt."""
        self.assertEqual(Solution().findTilt(None), 0)


if __name__ == "__main__":
    unittest.main()
