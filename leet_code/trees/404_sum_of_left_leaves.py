import unittest
from typing import Optional


# Definition for a binary tree node.
# This class represents a node in the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# The Solution class contains the main logic for calculating the sum.
class Solution:
    """
    Solution class to find the sum of all left leaves in a binary tree.
    """

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """
        Main method to initiate the traversal and calculate the sum.

        Args:
            root: The root node of the binary tree.

        Returns:
            The total sum of the values of all left leaves.
        """
        # Initialize the sum to 0. This will be updated during the traversal.
        self.sum = 0
        # Start the preorder traversal from the root.
        # The 'is_left' flag is initially False as the root itself is not a left child.
        self.preorder(root, False)
        # Return the final calculated sum.
        return self.sum

    def preorder(self, node: Optional[TreeNode], is_left: bool):
        """
        Performs a preorder traversal of the binary tree recursively.

        Args:
            node: The current node being visited.
            is_left: A boolean flag indicating if the current node is a left child of its parent.
        """
        # Base case: if the node is None, we simply return.
        if node:
            # Check if the current node is a leaf and a left child.
            # A node is a leaf if it has no left or right children.
            if node.left is None and node.right is None and is_left == True:
                # If it's a left leaf, add its value to the total sum.
                self.sum += node.val

            # Recursively call preorder for the left child.
            # The 'is_left' flag for the left child is set to True.
            if node.left:
                self.preorder(node.left, True)

            # Recursively call preorder for the right child.
            # The 'is_left' flag for the right child is set to False.
            if node.right:
                self.preorder(node.right, False)


# Unit tests to verify the Solution class
class TestSolution(unittest.TestCase):
    def test_example_tree(self):
        # Example from the problem description: [3,9,20,None,None,15,7]
        # The left leaves are 9 and 15, so the sum should be 24.
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(Solution().sumOfLeftLeaves(root), 24)

    def test_single_node(self):
        # A tree with only a root node. No left leaves exist.
        root = TreeNode(1)
        self.assertEqual(Solution().sumOfLeftLeaves(root), 0)

    def test_no_left_leaves(self):
        # A tree where nodes only have right children.
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(Solution().sumOfLeftLeaves(root), 0)

    def test_empty_tree(self):
        # An empty tree.
        root = None
        self.assertEqual(Solution().sumOfLeftLeaves(root), 0)

    def test_complex_tree(self):
        # A more complex tree with multiple left leaves.
        # Left leaves are: 6, 9, 11. Sum should be 6 + 9 + 11 = 26.
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        root.left.left.left.left = TreeNode(9)
        root.left.left.left.right = TreeNode(10)
        root.left.right.left = TreeNode(11)
        self.assertEqual(Solution().sumOfLeftLeaves(root), 26)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
