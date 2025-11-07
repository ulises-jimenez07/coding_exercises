"""
Problem: Find the level with the maximum sum in a binary tree

Approach:
- Use BFS to traverse tree level by level
- Track sum for each level and compare with max
- Return the smallest level number with maximum sum
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(w) where w is maximum width of tree
"""

import unittest
from collections import deque
from typing import Optional


class TreeNode:
    """A node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class to find the level with the maximum sum in a binary tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the level with the maximum sum in a binary tree using BFS.
        """
        if not root:
            return 0

        max_sum = float("-inf")
        max_level = 0
        level = 1
        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level
            level += 1

        return max_level


class TestMaxLevelSum(unittest.TestCase):
    """
    Unit tests for the maxLevelSum method.
    """

    def setUp(self):
        """
        Set up a new Solution object for each test.
        """
        self.solution = Solution()

    def test_example_tree(self):
        """
        Test case from the LeetCode example.
        """
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_single_node(self):
        """
        Test a tree with only one node.
        """
        root = TreeNode(10)
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_empty_tree(self):
        """
        Test an empty tree (root is None).
        """
        self.assertEqual(self.solution.maxLevelSum(None), 0)

    def test_all_negative_values(self):
        """
        Test a tree with all negative values.
        """
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(-4)
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_multiple_levels_with_same_max_sum(self):
        """
        Test where multiple levels have the same max sum; returns the smallest level.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(0)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(1)
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_imbalanced_tree(self):
        """
        Test an imbalanced tree.
        """
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(-4)
        self.assertEqual(self.solution.maxLevelSum(root), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
