import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """
    A class to represent a node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class containing methods to determine if a binary tree is height-balanced.
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is height-balanced.

        A height-balanced binary tree is a tree in which the depth of the two
        subtrees of every node never differs by more than one. This method
        calls a helper function `height` to check the balance.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the tree is height-balanced, False otherwise.
        """
        # The `height` helper function returns -1 if the tree is unbalanced
        # at any point, otherwise it returns the height.
        root_height = self.height(root)
        if root_height == -1:
            return False
        return True

    def height(self, node: Optional[TreeNode]) -> int:
        """
        Recursively calculates the height of a binary tree and checks for balance.

        This is a helper function that performs a post-order traversal. For each node,
        it calculates the height of its left and right subtrees. If at any point the
        height difference is greater than 1, it returns -1 to signal an imbalance.

        Args:
            node: The current node in the traversal.

        Returns:
            The height of the subtree rooted at `node` if it is balanced, or -1 if
            it is unbalanced.
        """
        # Base case: an empty tree has a height of 0.
        if node is None:
            return 0

        # Recursively get the height of the left and right subtrees.
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        # Check if either subtree is unbalanced (signaled by a -1 return)
        # or if the current node's subtrees are unbalanced.
        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        # If the subtrees are balanced, return the height of the current subtree.
        return max(left_height, right_height) + 1


# ------------------------------------------------------------------------------


class TestIsBalanced(unittest.TestCase):
    """
    Unit tests for the isBalanced method of the Solution class.
    """

    def setUp(self):
        """
        Set up a new instance of the Solution class for each test.
        """
        self.solution = Solution()

    def test_balanced_tree(self):
        """
        Tests a perfect, balanced binary tree.
        """
        # A simple balanced tree:
        #      3
        #     / \
        #    9  20
        #   / \
        #  1  2
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(2)
        self.assertTrue(self.solution.isBalanced(root))

    def test_unbalanced_tree(self):
        """
        Tests a binary tree that is not height-balanced.
        """
        # An unbalanced tree with a skewed left side:
        #       1
        #      /
        #     2
        #    /
        #   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_single_node_tree(self):
        """
        Tests a tree with a single node, which is always balanced.
        """
        root = TreeNode(1)
        self.assertTrue(self.solution.isBalanced(root))

    def test_empty_tree(self):
        """
        Tests an empty tree (root is None).
        """
        root = None
        self.assertTrue(self.solution.isBalanced(root))

    def test_right_skewed_tree(self):
        """
        Tests a tree skewed to the right to ensure the check is not biased.
        """
        # A right-skewed tree that is not balanced:
        # 1
        #  \
        #   2
        #    \
        #     3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertFalse(self.solution.isBalanced(root))

    def test_complex_balanced_tree(self):
        """
        Tests a more complex balanced tree.
        """
        # A complex balanced tree:
        #          1
        #        /   \
        #       2     2
        #      / \   / \
        #     3   3 3   3
        #    / \
        #   4   4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(3)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.left.left = TreeNode(4)
        root.left.left.right = TreeNode(4)
        self.assertTrue(self.solution.isBalanced(root))


if __name__ == "__main__":
    unittest.main()
