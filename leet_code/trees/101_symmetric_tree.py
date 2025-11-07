"""
Problem: Determine if a binary tree is a mirror of itself (symmetric around center)

Approach:
- Check if left subtree mirrors right subtree
- Recursively compare outer and inner nodes
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) for recursion stack, h is height
"""

import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True
        return self.is_mirror(root.left, root.right)

    def is_mirror(self, t1, t2):
        # Both subtrees empty, symmetric
        if t1 is None and t2 is None:
            return True
        # One empty, one not, not symmetric
        if t1 is None or t2 is None:
            return False

        # Check values match and mirror children
        return t1.val == t2.val and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)


class TestIsSymmetric(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_symmetric_tree(self):
        """Symmetric tree."""
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        self.assertTrue(self.solution.isSymmetric(root))

    def test_non_symmetric_tree(self):
        """Non-symmetric tree."""
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        self.assertFalse(self.solution.isSymmetric(root))

    def test_empty_tree(self):
        """Empty tree."""
        self.assertTrue(self.solution.isSymmetric(None))

    def test_single_node(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertTrue(self.solution.isSymmetric(root))

    def test_unequal_mirrored_values(self):
        """Unequal values at mirrored positions."""
        root = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(4)))
        self.assertFalse(self.solution.isSymmetric(root))


if __name__ == "__main__":
    unittest.main()
