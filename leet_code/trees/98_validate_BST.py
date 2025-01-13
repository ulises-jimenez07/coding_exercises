import unittest
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Represents a node in a binary tree.

        :param val: The value of the node.
        :param left: The left child node.
        :param right: The right child node.
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Checks if a given binary tree is a valid Binary Search Tree (BST).

        A BST is defined as follows:

        - The left subtree of a node contains only nodes with keys less than the node's key.
        - The right subtree of a node contains only nodes with keys greater than the node's key.
        - Both the left and right subtrees must also be valid BSTs.

        :param root: The root of the binary tree.
        :return: True if the tree is a valid BST, False otherwise.
        """

        def validate(node, low=-math.inf, high=math.inf):
            """
            Recursive helper function to validate BST properties.

            :param node: The current node being checked.
            :param low: The lower bound for the node's value.
            :param high: The upper bound for the node's value.
            :return: True if the subtree rooted at 'node' is a valid BST, False otherwise.
            """
            if not node:
                return True  # Empty subtree is valid

            if node.val <= low or node.val >= high:
                return False  # Node value violates BST property

            # Recursively check left and right subtrees with updated bounds
            return validate(node.right, node.val, high) and validate(
                node.left, low, node.val
            )

        return validate(root)


class TestIsValidBST(unittest.TestCase):
    def test_valid_bst(self):
        """Test cases with valid BSTs."""
        solution = Solution()

        # Test case 1: Simple valid BST
        root1 = TreeNode(2, TreeNode(1), TreeNode(3))
        self.assertTrue(solution.isValidBST(root1))

        # Test case 2: Larger valid BST
        root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        self.assertFalse(solution.isValidBST(root2))

    def test_invalid_bst(self):
        """Test cases with invalid BSTs."""
        solution = Solution()

        # Test case 3: Left child greater than root
        root3 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(solution.isValidBST(root3))

        # Test case 4: Right child less than root
        root4 = TreeNode(3, TreeNode(2), TreeNode(1))
        self.assertFalse(solution.isValidBST(root4))

        # Test case 5: Duplicate values
        root5 = TreeNode(2, TreeNode(2), TreeNode(3))
        self.assertFalse(solution.isValidBST(root5))

    def test_edge_cases(self):
        """Test edge cases like empty tree and single node tree."""
        solution = Solution()

        # Test case 6: Empty tree
        self.assertTrue(solution.isValidBST(None))

        # Test case 7: Single node tree
        root7 = TreeNode(1)
        self.assertTrue(solution.isValidBST(root7))


if __name__ == "__main__":
    unittest.main()
