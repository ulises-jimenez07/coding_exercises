"""
Problem: Find all root-to-leaf paths that sum to target value

Approach:
- Use DFS with backtracking to explore all paths
- Track current path and sum, copy path when target found
- Backtrack by popping from path after exploring each subtree
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) for path and recursion stack
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


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.answer: list[list[int]] = []
        self._pre_order(root, 0, [], targetSum)
        return self.answer

    def _pre_order(
        self,
        node: Optional[TreeNode],
        sum_till_parent: int,
        path_till_parent: List[int],
        target_sum: int,
    ):
        if node:
            current_sum = sum_till_parent + node.val
            path_till_parent.append(node.val)

            if node.left is None and node.right is None and current_sum == target_sum:
                self.answer.append(path_till_parent.copy())

            if node.left:
                self._pre_order(node.left, current_sum, path_till_parent, target_sum)
            if node.right:
                self._pre_order(node.right, current_sum, path_till_parent, target_sum)

            path_till_parent.pop()


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_paths(self):
        """Tree with multiple valid paths."""
        root = TreeNode(5)
        root.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
        root.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))

        expected = sorted([[5, 4, 11, 2], [5, 8, 4, 5]])
        actual = sorted(self.solution.pathSum(root, 22))
        self.assertEqual(actual, expected)

        self.assertEqual(sorted(self.solution.pathSum(root, 26)), sorted([[5, 8, 13]]))
        self.assertEqual(self.solution.pathSum(root, 30), [])

    def test_single_node(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.pathSum(root, 1), [[1]])
        self.assertEqual(self.solution.pathSum(root, 0), [])

    def test_empty_tree(self):
        """Empty tree."""
        self.assertEqual(self.solution.pathSum(None, 0), [])

    def test_simple_tree(self):
        """Simple tree with two children."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(sorted(self.solution.pathSum(root, 3)), sorted([[1, 2]]))
        self.assertEqual(sorted(self.solution.pathSum(root, 4)), sorted([[1, 3]]))
        self.assertEqual(self.solution.pathSum(root, 5), [])


if __name__ == "__main__":
    unittest.main()
