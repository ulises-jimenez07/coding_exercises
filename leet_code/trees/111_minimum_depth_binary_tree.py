"""
Problem: Find the minimum depth from root to nearest leaf node

Approach:
- Use recursion, handling one-child cases separately
- If node has only one child, depth is 1 + that child's depth
- If both children exist, return 1 + min(left, right)
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from collections import deque
from typing import (
    Deque,
    List,
    Optional,
)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def min_depth(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = min_depth(node.left)
            right_height = min_depth(node.right)

            if left_height == 0:
                return right_height + 1

            if right_height == 0:
                return left_height + 1

            return 1 + min(left_height, right_height)

        return min_depth(root)


class TestMinDepth(unittest.TestCase):
    def list_to_tree(self, arr: List[Optional[int]]) -> Optional[TreeNode]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue: Deque[TreeNode] = deque([root])
        i = 1
        n = len(arr)

        while queue and i < n:
            current_node = queue.popleft()

            if i < n and arr[i] is not None:
                current_node.left = TreeNode(arr[i])
                queue.append(current_node.left)
            i += 1

            if i < n and arr[i] is not None:
                current_node.right = TreeNode(arr[i])
                queue.append(current_node.right)
            i += 1

        return root

    def test_basic_tree(self):
        """Basic tree with min depth 2."""
        root = self.list_to_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(Solution().minDepth(root), 2)

    def test_single_node(self):
        """Single node tree."""
        root = self.list_to_tree([1])
        self.assertEqual(Solution().minDepth(root), 1)

    def test_empty_tree(self):
        """Empty tree."""
        root = self.list_to_tree([])
        self.assertEqual(Solution().minDepth(root), 0)

    def test_skewed_tree_left(self):
        """Left-skewed tree."""
        root = self.list_to_tree([1, 2, None, 3, None, None, None, 4])
        self.assertEqual(Solution().minDepth(root), 3)

    def test_skewed_tree_right(self):
        """Right-skewed tree."""
        root = self.list_to_tree([1, None, 2, None, None, None, 3, None, 4])
        self.assertEqual(Solution().minDepth(root), 2)

    def test_complex_tree(self):
        """Complex right-skewed tree."""
        root = self.list_to_tree([2, None, 3, None, 4, None, 5, None, 6])
        self.assertEqual(Solution().minDepth(root), 5)


if __name__ == "__main__":
    unittest.main()
