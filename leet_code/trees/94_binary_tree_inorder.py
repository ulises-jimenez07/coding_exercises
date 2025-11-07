"""
Problem: Perform inorder traversal of a binary tree

Approach:
- Recursively traverse: left subtree, root, right subtree
- Returns nodes in sorted order for BST
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
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
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


class TestInorderTraversal(unittest.TestCase):
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

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.inorderTraversal(None), [])

    def test_single_node_tree(self):
        """Tests a tree with a single node."""
        root = self.create_tree([10])
        self.assertEqual(self.solution.inorderTraversal(root), [10])

    def test_simple_tree(self):
        """Tests a simple tree."""
        root = self.create_tree([2, 1, 3])
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])

    def test_complex_tree(self):
        """Tests a complex tree."""
        root = self.create_tree([10, 5, 15, 3, 7, None, 20])
        self.assertEqual(self.solution.inorderTraversal(root), [3, 5, 7, 10, 15, 20])

    def test_skewed_left_tree(self):
        """Tests a left-skewed tree."""
        root = self.create_tree([5, 4, None, 3])
        self.assertEqual(self.solution.inorderTraversal(root), [3, 4, 5])

    def test_skewed_right_tree(self):
        """Tests a right-skewed tree."""
        root = self.create_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.inorderTraversal(root), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
