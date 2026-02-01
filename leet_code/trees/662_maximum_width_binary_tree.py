"""
Problem: Maximum Width of Binary Tree

Approach:
- Use level-order traversal (BFS) to track the position of each node.
- Assign indices to nodes: left child (2*i + 1), right child (2*i + 2).
- Width of a level is (rightmost_index - leftmost_index + 1).
- Time complexity: O(n) where n is the number of nodes.
- Space complexity: O(w) where w is the maximum width of the tree.
"""

import unittest
from collections import deque
from typing import (
    List,
    Optional,
)


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Class to find the maximum width of a binary tree."""

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """Calculates the maximum width of the binary tree."""
        if not root:
            return 0

        max_width = 0
        # Queue stores (node, index)
        queue = deque([(root, 0)])

        while queue:
            level_size = len(queue)
            left_most_index = queue[0][1]
            right_most_index = left_most_index

            # Process all nodes in current level
            for _ in range(level_size):
                node, i = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * i + 1))
                if node.right:
                    queue.append((node.right, 2 * i + 2))
                right_most_index = i

            # Update max width using indices of leftmost and rightmost nodes
            width = right_most_index - left_most_index + 1
            max_width = max(max_width, width)

        return max_width


class TestWidthOfBinaryTree(unittest.TestCase):
    """Test suite for widthOfBinaryTree function."""

    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper to create a binary tree from a list (level-order)."""
        if not values:
            return None
        root = TreeNode(values[0])
        queue = deque([root])
        i = 1
        while i < len(values):
            current = queue.popleft()
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
        self.assertEqual(self.solution.widthOfBinaryTree(None), 0)

    def test_single_node(self):
        """Tests a tree with only one node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.widthOfBinaryTree(root), 1)

    def test_example_1(self):
        """Tests LeetCode example 1."""
        #     1
        #    / \
        #   3   2
        #  / \   \
        # 5   3   9
        root = self.create_tree([1, 3, 2, 5, 3, None, 9])
        self.assertEqual(self.solution.widthOfBinaryTree(root), 4)

    def test_example_2(self):
        """Tests LeetCode example 2."""
        #     1
        #    / \
        #   3   2
        #  /     \
        # 5       9
        # /       /
        # 6       7
        root = self.create_tree([1, 3, 2, 5, None, None, 9, 6, None, 7])
        self.assertEqual(self.solution.widthOfBinaryTree(root), 7)

    def test_example_3(self):
        """Tests LeetCode example 3."""
        #   1
        #  / \
        # 3   2
        # /
        # 5
        root = self.create_tree([1, 3, 2, 5])
        self.assertEqual(self.solution.widthOfBinaryTree(root), 2)


if __name__ == "__main__":
    unittest.main()
