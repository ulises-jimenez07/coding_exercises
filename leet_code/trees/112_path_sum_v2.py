# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import unittest
from typing import Optional


# A placeholder for the TreeNode class, as it's typically provided by the platform
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class to find if a binary tree has a root-to-leaf path that sums to a target value.
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        The main public method to start the path sum search.
        It calls a private helper method with initial parameters.

        Args:
            root: The root node of the binary tree.
            targetSum: The target sum to be found.

        Returns:
            True if a path with the target sum exists, False otherwise.
        """
        return self._path_sum(root, 0, targetSum)

    def _path_sum(self, node: Optional[TreeNode], sum_till_parent: int, target_sum: int) -> bool:
        """
        A private recursive helper method to traverse the tree and calculate sums.

        Args:
            node: The current node being visited.
            sum_till_parent: The sum of node values from the root to the current node's parent.
            target_sum: The target sum we are trying to achieve.

        Returns:
            True if a path from the current node to a leaf equals the target sum, False otherwise.
        """
        # Base case 1: If the node is None, it's an invalid path, so we return False.
        if not node:
            return False

        # Base case 2: If it's a leaf node (no children).
        if node.left is None and node.right is None:
            # Calculate the total sum for this root-to-leaf path.
            current_sum = sum_till_parent + node.val
            # Check if this path's sum equals the target sum.
            return current_sum == target_sum

        # Recursive step: Update the sum for the current path.
        current_sum = sum_till_parent + node.val

        # Recurse on the left and right children.
        # The 'or' operator is used because we only need one path to satisfy the condition.
        left_result = self._path_sum(node.left, current_sum, target_sum)
        right_result = self._path_sum(node.right, current_sum, target_sum)

        return left_result or right_result


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_hasPathSum(self):
        """
        Tests the hasPathSum method with various tree configurations.
        """
        solution = Solution()

        # Test case 1: A simple tree with a path that sums to the target.
        # Tree:      5
        #           / \
        #          4   8
        #         /   / \
        #        11  13  4
        #       / \     \
        #      7   2     1
        root1 = TreeNode(5)
        root1.left = TreeNode(4)
        root1.right = TreeNode(8)
        root1.left.left = TreeNode(11)
        root1.left.left.left = TreeNode(7)
        root1.left.left.right = TreeNode(2)
        root1.right.left = TreeNode(13)
        root1.right.right = TreeNode(4)
        root1.right.right.right = TreeNode(1)

        self.assertTrue(
            solution.hasPathSum(root1, 22),
            "Test Case 1 Failed: Should be True for path 5->4->11->2",
        )
        self.assertTrue(
            solution.hasPathSum(root1, 26), "Test Case 1 Failed: Should be True for path 5->8->13"
        )
        self.assertFalse(solution.hasPathSum(root1, 28), "Test Case 1 Failed: Should be False")

        # Test case 2: A single-node tree.
        root2 = TreeNode(1)
        self.assertTrue(
            solution.hasPathSum(root2, 1),
            "Test Case 2 Failed: Should be True for single node tree",
        )
        self.assertFalse(solution.hasPathSum(root2, 0), "Test Case 2 Failed: Should be False")

        # Test case 3: An empty tree.
        root3 = None
        self.assertFalse(
            solution.hasPathSum(root3, 0), "Test Case 3 Failed: Should be False for an empty tree"
        )

        # Test case 4: A tree with a path sum not existing.
        # Tree:      1
        #           / \
        #          2   3
        root4 = TreeNode(1)
        root4.left = TreeNode(2)
        root4.right = TreeNode(3)
        self.assertFalse(
            solution.hasPathSum(root4, 5),
            "Test Case 4 Failed: Should be False as no path sums to 5",
        )
        self.assertTrue(
            solution.hasPathSum(root4, 3), "Test Case 4 Failed: Should be True for path 1->2"
        )
        self.assertTrue(
            solution.hasPathSum(root4, 4), "Test Case 4 Failed: Should be True for path 1->3"
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
