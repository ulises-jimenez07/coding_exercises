"""
Problem: Count good nodes where node value >= all ancestors

Approach:
- Track maximum value seen on path from root
- Node is good if its value >= current max
- Recursively count good nodes in both subtrees
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Solves the 'Good Nodes in Binary Tree' problem recursively.
    A node is 'good' if its value is the greatest on the path from the root.
    """

    def goodNodes(self, root: TreeNode) -> int:
        """Counts the number of good nodes in the binary tree."""

        def count_good_nodes(node, max_val):
            if not node:
                return 0

            # A node is good if its value is >= the max value on the path so far.
            is_good = 1 if node.val >= max_val else 0
            new_max = max(max_val, node.val)

            # Recursively count good nodes in the left and right subtrees.
            return is_good + count_good_nodes(node.left, new_max) + count_good_nodes(node.right, new_max)

        return count_good_nodes(root, float("-inf"))


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_simple_case(self):
        """Tests a simple binary tree with a mix of good and bad nodes."""
        root = TreeNode(3)
        root.left = TreeNode(1, TreeNode(3))
        root.right = TreeNode(4, TreeNode(1), TreeNode(5))
        self.assertEqual(self.solution.goodNodes(root), 4)

    def test_all_good(self):
        """Tests a tree where all nodes are good."""
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(self.solution.goodNodes(root), 3)

    def test_all_bad_except_root(self):
        """Tests a tree where only the root is a good node."""
        root = TreeNode(5, TreeNode(2), TreeNode(4))
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_single_node(self):
        """Tests a tree with only a single node."""
        root = TreeNode(10)
        self.assertEqual(self.solution.goodNodes(root), 1)

    def test_empty_tree(self):
        """Tests an empty tree."""
        root = None
        self.assertEqual(self.solution.goodNodes(root), 0)


if __name__ == "__main__":
    unittest.main()
