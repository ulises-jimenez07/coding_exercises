"""
Problem: Flatten binary tree to linked list in-place using preorder

Approach:
- Recursively flatten left and right subtrees
- Connect left subtree's tail to right subtree
- Move left subtree to right and set left to None
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root) -> None:
        def flatten_tree(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node

            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)

            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tail if right_tail else left_tail

        flatten_tree(root)


class TestFlatten(unittest.TestCase):
    def test_flatten(self):
        """Standard tree flattening."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right = TreeNode(5)
        root.right.right = TreeNode(6)

        solution = Solution()
        solution.flatten(root)

        expected = [1, 2, 3, 4, 5, 6]
        result = []
        current = root
        while current:
            result.append(current.val)
            current = current.right

        self.assertEqual(result, expected)

    def test_single_node(self):
        """Single node tree."""
        root = TreeNode(1)

        solution = Solution()
        solution.flatten(root)

        self.assertEqual(root.val, 1)
        self.assertIsNone(root.left)
        self.assertIsNone(root.right)

    def test_empty_tree(self):
        """Empty tree."""
        solution = Solution()
        solution.flatten(None)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
