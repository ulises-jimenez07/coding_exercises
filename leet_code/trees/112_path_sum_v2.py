"""
Problem: Check if tree has root-to-leaf path that sums to target (alternative approach)

Approach:
- Track running sum from root instead of subtracting
- At leaf nodes, compare accumulated sum with target
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self._path_sum(root, 0, targetSum)

    def _path_sum(self, node: Optional[TreeNode], sum_till_parent: int, target_sum: int) -> bool:
        if not node:
            return False

        if node.left is None and node.right is None:
            current_sum = sum_till_parent + node.val
            return current_sum == target_sum

        current_sum = sum_till_parent + node.val

        left_result = self._path_sum(node.left, current_sum, target_sum)
        right_result = self._path_sum(node.right, current_sum, target_sum)

        return left_result or right_result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_valid_path_sum(self):
        """Tree with valid path sums."""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        self.assertTrue(self.solution.hasPathSum(root, 22))
        self.assertTrue(self.solution.hasPathSum(root, 26))
        self.assertFalse(self.solution.hasPathSum(root, 28))

    def test_single_node_tree(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 1))
        self.assertFalse(self.solution.hasPathSum(root, 0))

    def test_empty_tree(self):
        """Empty tree."""
        self.assertFalse(self.solution.hasPathSum(None, 0))

    def test_no_valid_path(self):
        """Tree with no path matching target sum."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(self.solution.hasPathSum(root, 5))
        self.assertTrue(self.solution.hasPathSum(root, 3))
        self.assertTrue(self.solution.hasPathSum(root, 4))


if __name__ == "__main__":
    unittest.main()
