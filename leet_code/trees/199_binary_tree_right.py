"""
Problem: Return the right side view of a binary tree

Approach:
- Use BFS to traverse level by level
- Capture the last node value at each level
- This represents what's visible from the right
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(w) where w is maximum width of tree
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """Returns the right side view of a binary tree using BFS."""
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # Add the last node of each level to the result.
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


class TestRightSideView(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_tree(self):
        """Tests a standard tree structure."""
        root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 4])

    def test_single_node(self):
        """Tests a tree with only a single node."""
        root = TreeNode(1)
        self.assertEqual(self.solution.rightSideView(root), [1])

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.rightSideView(None), [])

    def test_full_binary_tree(self):
        """Tests a full binary tree."""
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
        self.assertEqual(self.solution.rightSideView(root), [1, 3, 7])

    def test_left_skewed_tree(self):
        """Tests a tree that is skewed to the left."""
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        self.assertEqual(self.solution.rightSideView(root), [1, 2, 3])

    def test_right_skewed_tree(self):
        """Tests a tree that is skewed to the right."""
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.solution.rightSideView(root), [1, 2, 3])

    def test_complex_tree(self):
        """Tests a more complex tree structure."""
        root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7, TreeNode(6))), TreeNode(15, None, TreeNode(18)))
        self.assertEqual(self.solution.rightSideView(root), [10, 15, 18, 6])


if __name__ == "__main__":
    unittest.main()
