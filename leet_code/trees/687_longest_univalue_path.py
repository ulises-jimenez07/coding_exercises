"""
Problem: Find the longest path where all nodes have the same value.

Approach:
- Use depth-first search to compute the longest downward same-value path.
- For each node, extend left/right paths only if child value matches node value.
- Update a running maximum with left_extension + right_extension at each node.
- Time complexity: O(n) where n is number of nodes.
- Space complexity: O(h) where h is tree height (recursion stack).
"""

import unittest
from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node used for univalue path computations."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Computes the longest path containing a single repeated value."""

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal longest
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            left_count = 0
            right_count = 0

            # Extend left path only when values match.
            if node.left and node.left.val == node.val:
                left_count = left + 1

            # Extend right path only when values match.
            if node.right and node.right.val == node.val:
                right_count = right + 1

            # Candidate path passes through current node.
            longest = max(longest, left_count + right_count)
            return max(left_count, right_count)

        dfs(root)
        return longest


class TestSolution(unittest.TestCase):
    """Unit tests for longest-univalue-path solution."""

    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: list) -> Optional[TreeNode]:
        if not values:
            return None

        root = TreeNode(values[0])
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            current = queue.popleft()

            if index < len(values) and values[index] is not None:
                current.left = TreeNode(values[index])
                queue.append(current.left)
            index += 1

            if index < len(values) and values[index] is not None:
                current.right = TreeNode(values[index])
                queue.append(current.right)
            index += 1

        return root

    def test_example_one(self):
        """Tests a tree where the longest path goes through the left subtree."""
        root = self.create_tree([5, 4, 5, 1, 1, None, 5])
        self.assertEqual(self.solution.longestUnivaluePath(root), 2)

    def test_example_two(self):
        """Tests a tree where the longest path goes through both children."""
        root = self.create_tree([1, 4, 5, 4, 4, None, 5])
        self.assertEqual(self.solution.longestUnivaluePath(root), 2)

    def test_all_same_values(self):
        """Tests a full tree where all values are equal."""
        root = self.create_tree([1, 1, 1, 1, 1, 1, 1])
        self.assertEqual(self.solution.longestUnivaluePath(root), 4)

    def test_single_node_tree(self):
        """Tests a tree with only one node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.longestUnivaluePath(root), 0)

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.longestUnivaluePath(None), 0)


if __name__ == "__main__":
    unittest.main()
