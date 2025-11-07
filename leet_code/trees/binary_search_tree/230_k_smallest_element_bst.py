"""
Problem: Find the k-th smallest element in a Binary Search Tree

Approach:
- Use inorder traversal which visits BST nodes in sorted order
- Stop traversal once k-th element is found for efficiency
- Track count during traversal to identify k-th position
- Time complexity: O(k) in best case, O(n) worst case
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.

    Attributes:
        val (int): The value of the node.
        left (TreeNode): The left child node.
        right (TreeNode): The right child node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Finds the k-th smallest element in a Binary Search Tree (BST).
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Finds the k-th smallest element in the BST using an inorder traversal.

        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
            k (int): The k-th position of the smallest element to find.

        Returns:
            int: The value of the k-th smallest element.
        """
        self.k = k
        self.count = 0
        self.ans = None
        self.inorder(root)
        return self.ans

    def inorder(self, node: Optional[TreeNode]):
        """
        Performs an inorder traversal of the tree to find the k-th element.

        The inorder traversal of a BST visits nodes in increasing order of their values.
        This method stops the traversal once the k-th element is found to optimize performance.

        Args:
            node (Optional[TreeNode]): The current node being visited.
        """
        # If the answer is already found, we can stop the traversal.
        if self.ans is not None:
            return

        # Traverse the left subtree.
        if node.left:
            self.inorder(node.left)

        # Check if the answer has already been found after the left traversal
        # to avoid unnecessary computations on the right side.
        if self.ans is not None:
            return

        # Visit the current node.
        self.count += 1
        if self.count == self.k:
            self.ans = node.val
            return

        # Traverse the right subtree.
        if node.right:
            self.inorder(node.right)


class TestKthSmallest(unittest.TestCase):
    """
    Unit tests for the Solution.kthSmallest method.
    """

    def test_example_1(self):
        """
        Test case from LeetCode example 1.
        Tree: [3,1,4,None,2]
        k = 1
        Expected: 1
        """
        # Create the tree:
        #   3
        #  / \
        # 1   4
        #  \
        #   2
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)

        solution = Solution()
        self.assertEqual(solution.kthSmallest(root, 1), 1)

    def test_example_2(self):
        """
        Test case from LeetCode example 2.
        Tree: [5,3,6,2,4,None,None,1]
        k = 3
        Expected: 3
        """
        # Create the tree:
        #       5
        #      / \
        #     3   6
        #    / \
        #   2   4
        #  /
        # 1
        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(6)
        root.left.left = TreeNode(2)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(1)

        solution = Solution()
        self.assertEqual(solution.kthSmallest(root, 3), 3)

    def test_single_node(self):
        """
        Test case for a tree with a single node.
        Tree: [10]
        k = 1
        Expected: 10
        """
        root = TreeNode(10)
        solution = Solution()
        self.assertEqual(solution.kthSmallest(root, 1), 10)

    def test_large_k(self):
        """
        Test case for k being the largest element.
        Tree: [3,1,4,None,2]
        k = 4
        Expected: 4
        """
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)

        solution = Solution()
        self.assertEqual(solution.kthSmallest(root, 4), 4)

    def test_non_existent_k(self):
        """
        Test case for k being larger than the number of nodes.
        Tree: [3,1,4,None,2]
        k = 5
        Expected: None (or handling a scenario where the value isn't found).
        """
        root = TreeNode(3)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.left.right = TreeNode(2)

        solution = Solution()
        # The current implementation will return None if k is too large.
        self.assertIsNone(solution.kthSmallest(root, 5))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
