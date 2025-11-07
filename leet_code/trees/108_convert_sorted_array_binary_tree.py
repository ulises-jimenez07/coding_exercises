"""
Problem: Convert a sorted array to a height-balanced binary search tree

Approach:
- Use middle element as root to ensure balance
- Recursively build left and right subtrees from array halves
- Time complexity: O(n) where n is array length
- Space complexity: O(log n) for recursion stack in balanced tree
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def inorder(left, right):
            if left > right:
                return None

            mid = (left + right) // 2
            root = TreeNode(nums[mid])

            root.left = inorder(left, mid - 1)
            root.right = inorder(mid + 1, right)

            return root

        return inorder(0, len(nums) - 1)


def inorder_traversal(root: Optional[TreeNode], result: List[int]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)


def is_balanced_bst(root: Optional[TreeNode]) -> bool:
    traversal_result: list[int] = []
    inorder_traversal(root, traversal_result)

    def check_balance(node: Optional[TreeNode]):
        if not node:
            return 0

        left_height = check_balance(node.left)
        right_height = check_balance(node.right)

        if left_height == -1 or right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    is_balanced = check_balance(root) != -1

    return is_balanced and True


class TestSortedArrayToBST(unittest.TestCase):
    def test_simple_case(self):
        """Simple sorted array."""
        nums = [-10, -3, 0, 5, 9]
        solution = Solution()
        root = solution.sortedArrayToBST(nums)

        self.assertTrue(root is not None)
        self.assertTrue(is_balanced_bst(root))

        traversal_result = []
        inorder_traversal(root, traversal_result)
        self.assertEqual(traversal_result, nums)

    def test_empty_array(self):
        """Empty array."""
        nums = []
        solution = Solution()
        root = solution.sortedArrayToBST(nums)
        self.assertIsNone(root)

    def test_even_elements(self):
        """Array with even number of elements."""
        nums = [1, 2, 3, 4, 5, 6]
        solution = Solution()
        root = solution.sortedArrayToBST(nums)

        self.assertTrue(is_balanced_bst(root))

        traversal_result = []
        inorder_traversal(root, traversal_result)
        self.assertEqual(traversal_result, nums)


if __name__ == "__main__":
    unittest.main()
