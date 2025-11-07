"""
Problem: Find lowest common ancestor of two nodes in a BST

Approach:
- Use BST property: all left descendants < node < right descendants
- If both nodes < current, LCA is in left subtree
- If both nodes > current, LCA is in right subtree
- Otherwise, current node is the LCA (split point)
- Time complexity: O(h) where h is height of tree
- Space complexity: O(h) for recursion stack
"""

import unittest


# Definition for a binary tree node.
class TreeNode:
    """
    A class representing a node in a binary tree.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    A class containing the solution to find the lowest common ancestor in a BST.
    """

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        """
        Finds the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).

        The LCA of two nodes p and q is the lowest node in the tree that has both p and q as descendants
        (where we allow a node to be a descendant of itself).

        Args:
            root: The root node of the BST.
            p: The first node.
            q: The second node.

        Returns:
            The lowest common ancestor of p and q.
        """
        # If both p and q are in the left subtree, recurse on the left subtree.
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # If both p and q are in the right subtree, recurse on the right subtree.
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # This is the split point. The current root is the LCA.
        # This occurs when:
        # 1. p is on one side and q is on the other.
        # 2. The current root is either p or q.
        return root


# -----------------------------------------------------------------------------

## Unittest Suite


class TestLowestCommonAncestor(unittest.TestCase):
    """
    Test suite for the lowestCommonAncestor method.
    """

    def test_lca_in_the_middle(self):
        """
        Test case where the LCA is a node between p and q.
        """

        # Tree structure:
        #       6
        #      / \
        #     2   8
        #    / \ / \
        #   0  4 7  9
        #      / \
        #     3   5
        # LCA of 2 and 8 is 6.

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left  # Node with value 2
        q = root.right  # Node with value 8
        lca = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 6)

    def test_lca_is_one_of_the_nodes(self):
        """
        Test case where one of the nodes (p) is the LCA of itself and another node (q).
        """

        # Tree structure (same as above):
        #       6
        #      / \
        #     2   8
        #    / \ / \
        #   0  4 7  9
        #      / \
        #     3   5
        # LCA of 2 and 4 is 2.

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left  # Node with value 2
        q = root.left.right  # Node with value 4
        lca = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 2)

    def test_lca_is_root(self):
        """
        Test case where the LCA is the root of the entire tree.
        """

        # Tree structure:
        #       6
        #      / \
        #     2   8
        # LCA of 2 and 8 is 6.
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)

        p = root.left  # Node with value 2
        q = root.right  # Node with value 8
        lca = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 6)

    def test_lca_deep_in_tree(self):
        """
        Test case where the LCA is deep within the tree.
        """

        # Tree structure (same as above):
        #       6
        #      / \
        #     2   8
        #    / \ / \
        #   0  4 7  9
        #      / \
        #     3   5
        # LCA of 3 and 5 is 4.

        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left.right.left  # Node with value 3
        q = root.left.right.right  # Node with value 5
        lca = Solution().lowestCommonAncestor(root, p, q)
        self.assertEqual(lca.val, 4)


if __name__ == "__main__":
    unittest.main()
