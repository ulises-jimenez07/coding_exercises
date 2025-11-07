"""
Problem: Calculate the sum of all left leaves in a binary tree

Approach:
- Recursively traverse tree, identifying left leaf nodes
- Left leaf has no children and is a left child of parent
- Sum up values of identified left leaves
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # If the left child is a leaf, add its value.
        if root.left and not root.left.left and not root.left.right:
            left_sum = root.left.val
        else:
            left_sum = 0

        # Recurse on both children and sum the results.
        return left_sum + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)


class TestSolution(unittest.TestCase):
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

    def test_example_tree(self):
        """Tests a standard tree with left leaves."""
        root = self.create_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 24)

    def test_single_node(self):
        """Tests a tree with a single node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_no_left_leaves(self):
        """Tests a right-skewed tree with no left leaves."""
        root = self.create_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 0)

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.sumOfLeftLeaves(None), 0)

    def test_complex_tree(self):
        """Tests a complex tree with multiple left leaves."""
        root = self.create_tree([1, 2, 3, 4, 5, 6, 7, 8, None, 10, None, None, None, None, None, 9])
        self.assertEqual(self.solution.sumOfLeftLeaves(root), 25)  # 9 + 10 + 6


if __name__ == "__main__":
    unittest.main()
