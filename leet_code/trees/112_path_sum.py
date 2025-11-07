"""
Problem: Check if tree has root-to-leaf path that sums to target

Approach:
- Use recursion, subtracting current value from target
- At leaf node, check if remaining sum equals node value
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        """
        Checks if a root-to-leaf path sums up to the target.
        """
        if not root:
            return False

        # Check if it's a leaf node and if the value matches the remaining sum
        if not root.left and not root.right:
            return root.val == targetSum

        # Recursively check the left and right subtrees
        remaining_sum = targetSum - root.val
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)


import unittest


class TestHasPathSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_path_exists(self):
        """Test case where a valid path exists."""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.right = TreeNode(8)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 22))

    def test_path_does_not_exist(self):
        """Test case where no valid path exists."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(self.solution.hasPathSum(root, 5))

    def test_empty_tree(self):
        """Test with an empty tree."""
        self.assertFalse(self.solution.hasPathSum(None, 0))

    def test_single_node_match(self):
        """Test a single-node tree with a matching target."""
        root = TreeNode(1)
        self.assertTrue(self.solution.hasPathSum(root, 1))

    def test_single_node_no_match(self):
        """Test a single-node tree with a non-matching target."""
        root = TreeNode(1)
        self.assertFalse(self.solution.hasPathSum(root, 0))


if __name__ == "__main__":
    unittest.main()
