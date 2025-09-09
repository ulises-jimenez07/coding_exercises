import math
import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """
    A class representing a node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class containing the solution to validate a Binary Search Tree (BST).
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a given binary tree is a valid Binary Search Tree.

        A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with values less than the node's value.
        - The right subtree of a node contains only nodes with values greater than the node's value.
        - Both the left and right subtrees must also be valid BSTs.
        - There are no duplicate values.

        Args:
            root: The root node of the binary tree.

        Returns:
            True if the binary tree is a valid BST, False otherwise.
        """

        def validate(node, low=-math.inf, high=math.inf):
            """
            Recursive helper function to validate the BST property.

            Args:
                node: The current node being validated.
                low: The lower bound for the current node's value.
                high: The upper bound for the current node's value.

            Returns:
                True if the subtree rooted at 'node' is a valid BST, False otherwise.
            """
            # Base case: an empty node is a valid BST
            if not node:
                return True

            # Check if the current node's value is within the valid range
            if not (low < node.val < high):
                return False

            # Recursively validate the left and right subtrees with updated bounds
            # For the right subtree, the new lower bound is the current node's value.
            # For the left subtree, the new upper bound is the current node's value.
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        # Start the validation from the root with initial bounds of negative and positive infinity
        return validate(root)


# -----------------------------------------------------------------------------

## Unittest Suite


class TestIsValidBST(unittest.TestCase):
    """
    Test suite for the isValidBST method.
    """

    def test_valid_bst(self):
        """
        Test case for a valid BST.
        
        Tree structure:
             2
            / \
           1   3
        """
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(Solution().isValidBST(root))

    def test_invalid_bst(self):
        """
        Test case for an invalid BST where a left child is greater than the parent.
        
        Tree structure:
             5
            / \
           1   4
              / \
             3   6
        """
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(Solution().isValidBST(root))

    def test_empty_tree(self):
        """
        Test case for an empty tree, which is considered a valid BST.
        """
        self.assertTrue(Solution().isValidBST(None))

    def test_single_node(self):
        """
        Test case for a single-node tree, which is always a valid BST.
        """
        root = TreeNode(42)
        self.assertTrue(Solution().isValidBST(root))

    def test_duplicates(self):
        """
        Test case with duplicate values, which makes the BST invalid.
        
        Tree structure:
             2
            / \
           2   3
        """
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertFalse(Solution().isValidBST(root))

    def test_left_subtree_invalid(self):
        """
        Test case where a node in the left subtree is out of its valid range.
        
        Tree structure:
             5
            / \
           2   8
          / \
         1   6
        """
        root = TreeNode(5)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(6)  # 6 is greater than 5, so invalid
        self.assertFalse(Solution().isValidBST(root))


if __name__ == "__main__":
    unittest.main()
