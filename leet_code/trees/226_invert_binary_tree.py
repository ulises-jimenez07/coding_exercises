"""
Problem: Invert a binary tree (mirror it horizontally)

Approach:
- Recursively swap left and right children at each node
- Use one-line swap with tuple unpacking
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Solution class for inverting a binary tree."""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Main method to invert a binary tree. Calls the bottom-up recursive version."""
        return self.invert_tree_recursive_bottom_up(root)

    def invert_tree_recursive_bottom_up(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Inverts a binary tree recursively starting from the leaves."""
        if root:
            root.left, root.right = self.invert_tree_recursive_bottom_up(
                root.right
            ), self.invert_tree_recursive_bottom_up(root.left)
        return root

    def invert_tree_recursive_top_down(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """Inverts a binary tree recursively (top-down)."""
        if not root:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert left and right subtrees
        self.invert_tree_recursive_top_down(root.left)
        self.invert_tree_recursive_top_down(root.right)

        return root


# Helper functions for creating and serializing trees for testing.
def create_tree(nodes: list[Optional[int]]) -> Optional[TreeNode]:
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current_node = queue.pop(0)
        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root


def serialize_tree(root: Optional[TreeNode]) -> list[Optional[int]]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result


class TestInvertTree(unittest.TestCase):
    """Unit tests for the invertTree solution."""

    def setUp(self):
        self.solution = Solution()

    def test_example_case(self):
        """Tests a standard tree inversion."""
        root = create_tree([4, 2, 7, 1, 3, 6, 9])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [4, 7, 2, 9, 6, 3, 1])

    def test_top_down_version(self):
        """Tests the top-down recursive version."""
        root = create_tree([4, 2, 7, 1, 3, 6, 9])
        inverted_root = self.solution.invert_tree_recursive_top_down(root)
        self.assertEqual(serialize_tree(inverted_root), [4, 7, 2, 9, 6, 3, 1])

    def test_empty_tree(self):
        """Tests an empty tree."""
        root = create_tree([])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [])

    def test_single_node_tree(self):
        """Tests a tree with a single node."""
        root = create_tree([1])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [1])

    def test_unbalanced_tree(self):
        """Tests an unbalanced tree."""
        root = create_tree([1, 2])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [1, None, 2])

    def test_complex_tree(self):
        """Tests a complex, multi-level tree."""
        root = create_tree([10, 5, 15, 2, 7, 12, 17])
        inverted_root = self.solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [10, 15, 5, 17, 12, 7, 2])


if __name__ == "__main__":
    unittest.main()
