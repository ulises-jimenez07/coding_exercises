from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Finds the maximum path sum in a binary tree.

        A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

        The path sum of a path is the sum of the node's values in the path.

        Args:
            root: The root of the binary tree.

        Returns:
            The maximum path sum.
        """
        self.ans = -float("inf")  # Initialize the maximum path sum to negative infinity

        def solution(node):
            """
            Recursive helper function to calculate the maximum path sum starting from a given node.

            Args:
                node: The current node being considered.

            Returns:
                The maximum path sum starting from the given node.
            """
            if node is None:
                return 0  # Base case: empty subtree

            left = solution(
                node.left
            )  # Recursively calculate max path sum from left subtree
            right = solution(
                node.right
            )  # Recursively calculate max path sum from right subtree

            # Calculate the maximum path sum that includes the current node
            mx_side = max(
                node.val, node.val + max(left, right)
            )  # Max path ending at current node
            mx_current = max(
                mx_side, node.val + left + right
            )  # Max path including current node

            self.ans = max(self.ans, mx_current)  # Update the overall maximum path sum

            return mx_side  # Return the maximum path sum ending at the current node

        solution(root)  # Call the recursive helper function starting from the root
        return self.ans


import unittest


class TestMaxPathSum(unittest.TestCase):
    def test_max_path_sum(self):
        solution = Solution()

        # Test case 1: Example 1
        root1 = TreeNode(-10)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(solution.maxPathSum(root1), 42)

        # Test case 2: Example 2
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.right = TreeNode(3)
        self.assertEqual(solution.maxPathSum(root2), 6)

        # Test case 3: Negative values
        root3 = TreeNode(-3)
        self.assertEqual(solution.maxPathSum(root3), -3)

        # Test case 4: Single node
        root4 = TreeNode(5)
        self.assertEqual(solution.maxPathSum(root4), 5)

        # Test case 5: Skewed tree
        root5 = TreeNode(1)
        root5.left = TreeNode(2)
        root5.left.left = TreeNode(3)
        root5.left.left.left = TreeNode(4)
        self.assertEqual(solution.maxPathSum(root5), 10)

        # Test case 6: Empty tree
        self.assertEqual(solution.maxPathSum(None), -float("inf"))


if __name__ == "__main__":
    unittest.main()
