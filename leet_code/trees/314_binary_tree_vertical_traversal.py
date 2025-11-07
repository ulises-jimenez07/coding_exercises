"""
Problem: Return vertical order traversal of a binary tree

Approach:
- Use BFS with column indices (left=-1, right=+1)
- Store nodes in hash map by column index
- Sort columns and return values in order
- Time complexity: O(n log k) where k is number of columns
- Space complexity: O(n) for queue and hash map
"""

import unittest
from collections import (
    defaultdict,
    deque,
)
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
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # A hash map stores nodes by column index.
        column_hash = defaultdict(list)
        # The queue stores tuples of (node, column) for BFS.
        queue = deque([(root, 0)])

        while queue:
            curr, column = queue.popleft()
            column_hash[column].append(curr.val)

            if curr.left:
                queue.append((curr.left, column - 1))
            if curr.right:
                queue.append((curr.right, column + 1))

        # Sort the columns and return the values.
        return [column_hash[x] for x in sorted(column_hash.keys())]


class TestVerticalOrder(unittest.TestCase):
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

    def test_standard_traversal(self):
        """Tests a standard vertical traversal."""
        root = self.create_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(self.solution.verticalOrder(root), [[9], [3, 15], [20], [7]])

    def test_full_binary_tree(self):
        """Tests a full binary tree."""
        root = self.create_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.solution.verticalOrder(root), [[4], [2], [1, 5, 6], [3], [7]])

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.verticalOrder(None), [])

    def test_single_node(self):
        """Tests a tree with a single node."""
        root = self.create_tree([1])
        self.assertEqual(self.solution.verticalOrder(root), [[1]])

    def test_left_skewed_tree(self):
        """Tests a left-skewed tree."""
        root = self.create_tree([1, 2, None, 3])
        self.assertEqual(self.solution.verticalOrder(root), [[3], [2], [1]])


if __name__ == "__main__":
    unittest.main()
