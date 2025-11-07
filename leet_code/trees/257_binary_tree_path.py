"""
Problem: Find all root-to-leaf paths in a binary tree

Approach:
- Use DFS to explore all paths from root to leaves
- Build path string with arrows between nodes
- Add complete path when reaching a leaf node
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        paths: list[str] = []
        self.construct_paths(root, "", paths)
        return paths

    def construct_paths(self, node, path, paths):
        # Append the current node's value to the path
        path += str(node.val)

        # If it's a leaf node, the path is complete.
        if not node.left and not node.right:
            paths.append(path)
            return

        # Continue to children, adding an arrow for the next level.
        path += "->"
        if node.left:
            self.construct_paths(node.left, path, paths)
        if node.right:
            self.construct_paths(node.right, path, paths)


class TestBinaryTreePaths(unittest.TestCase):
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
        self.assertEqual(self.solution.binaryTreePaths(None), [])

    def test_single_node(self):
        """Tests a tree with a single node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.binaryTreePaths(root), ["1"])

    def test_simple_tree(self):
        """Tests a simple tree with two branches."""
        root = self.create_tree([1, 2, 3])
        self.assertEqual(sorted(self.solution.binaryTreePaths(root)), sorted(["1->2", "1->3"]))

    def test_complex_tree(self):
        """Tests a more complex tree structure."""
        root = self.create_tree([1, 2, 3, None, 5])
        self.assertEqual(sorted(self.solution.binaryTreePaths(root)), sorted(["1->2->5", "1->3"]))

    def test_left_skewed_tree(self):
        """Tests a tree that is skewed to the left."""
        root = self.create_tree([1, 2, None, 3])
        self.assertEqual(self.solution.binaryTreePaths(root), ["1->2->3"])

    def test_right_skewed_tree(self):
        """Tests a tree that is skewed to the right."""
        root = self.create_tree([1, None, 2, None, 3])
        self.assertEqual(self.solution.binaryTreePaths(root), ["1->2->3"])


if __name__ == "__main__":
    unittest.main()
