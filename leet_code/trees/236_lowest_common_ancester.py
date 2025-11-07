"""
Problem: Find the lowest common ancestor of two nodes in binary tree

Approach:
- Use post-order DFS to search for both nodes
- If both found in different subtrees, current node is LCA
- If only one found, that subtree contains the LCA
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q:
            return root

        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are in different subtrees, the current root is the LCA.
        if left_lca and right_lca:
            return root

        # Otherwise, the LCA is in whichever subtree it was found.
        return left_lca if left_lca else right_lca


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
        # Simple tree structure for testing
        self.root = TreeNode(3)
        self.root.left = TreeNode(5)
        self.root.right = TreeNode(1)
        self.root.left.left = TreeNode(6)
        self.root.left.right = TreeNode(2)
        self.root.right.left = TreeNode(0)
        self.root.right.right = TreeNode(8)
        self.root.left.right.left = TreeNode(7)
        self.root.left.right.right = TreeNode(4)

    def test_lca_in_different_subtrees(self):
        """Nodes in left and right subtrees."""
        p = self.root.left  # 5
        q = self.root.right  # 1
        self.assertEqual(self.solution.lowestCommonAncestor(self.root, p, q), self.root)

    def test_lca_is_one_of_the_nodes(self):
        """One node is an ancestor of the other."""
        p = self.root.left  # 5
        q = self.root.left.right.right  # 4
        self.assertEqual(self.solution.lowestCommonAncestor(self.root, p, q), p)

    def test_lca_is_root(self):
        """The root is one of the nodes."""
        p = self.root
        q = self.root.left.right.right  # 4
        self.assertEqual(self.solution.lowestCommonAncestor(self.root, p, q), self.root)

    def test_empty_tree(self):
        """Test with an empty tree."""
        self.assertIsNone(self.solution.lowestCommonAncestor(None, TreeNode(1), TreeNode(2)))


if __name__ == "__main__":
    unittest.main()
