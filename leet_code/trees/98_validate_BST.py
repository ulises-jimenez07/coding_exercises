"""
Problem: Validate if a binary tree is a valid Binary Search Tree

Approach:
- Track valid range (low, high) for each node value
- For left child: update high to current value
- For right child: update low to current value
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import math
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._validate(root, -math.inf, math.inf)

    def _validate(self, node, low, high):
        if not node:
            return True

        if not (low < node.val < high):
            return False

        return self._validate(node.left, low, node.val) and self._validate(node.right, node.val, high)


class TestIsValidBST(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
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

    def test_valid_bst(self):
        """Tests a simple, valid BST."""
        root = self.create_tree([2, 1, 3])
        self.assertTrue(self.solution.isValidBST(root))

    def test_invalid_bst_left_child(self):
        """Tests an invalid BST where a left child is greater than its parent."""
        root = self.create_tree([1, 2, 3])
        self.assertFalse(self.solution.isValidBST(root))

    def test_invalid_bst_right_child(self):
        """Tests an invalid BST where a right child is less than its parent."""
        root = self.create_tree([3, 2, 1])
        self.assertFalse(self.solution.isValidBST(root))

    def test_invalid_bst_duplicate_values(self):
        """Tests an invalid BST with duplicate values."""
        root = self.create_tree([2, 2, 3])
        self.assertFalse(self.solution.isValidBST(root))

    def test_invalid_bst_complex(self):
        """Tests a more complex invalid BST."""
        root = self.create_tree([5, 1, 4, None, None, 3, 6])
        self.assertFalse(self.solution.isValidBST(root))

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertTrue(self.solution.isValidBST(None))

    def test_single_node_tree(self):
        """Tests a tree with a single node."""
        root = self.create_tree([1])
        self.assertTrue(self.solution.isValidBST(root))


if __name__ == "__main__":
    unittest.main()
