"""
Problem: Find sum of BST nodes within a given range [low, high]

Approach:
- Use BST properties to skip entire subtrees
- If node < low, only check right subtree
- If node > high, only check left subtree
- Time complexity: O(n) worst case, better with pruning
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)

        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)


class TestRangeSumBST(unittest.TestCase):
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

    def test_example_1(self):
        """Tests the first example case."""
        root = self.create_tree([10, 5, 15, 3, 7, None, 18])
        self.assertEqual(self.solution.rangeSumBST(root, 7, 15), 32)

    def test_example_2(self):
        """Tests the second example case."""
        root = self.create_tree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
        self.assertEqual(self.solution.rangeSumBST(root, 6, 10), 23)

    def test_empty_tree(self):
        """Tests an empty tree."""
        self.assertEqual(self.solution.rangeSumBST(None, 0, 100), 0)


if __name__ == "__main__":
    unittest.main()
