import unittest
from typing import Optional, List


# A placeholder for the TreeNode class, typically provided by the platform
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class to find all root-to-leaf paths in a binary tree that sum to a target value.
    """

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        The main public method to find all paths. It initializes a list to store the results
        and calls a private helper method to perform the traversal.

        Args:
            root: The root node of the binary tree.
            targetSum: The target sum to be found.

        Returns:
            A list of lists, where each inner list represents a valid root-to-leaf path.
        """
        self.answer = []
        # We start the traversal from the root with an initial sum of 0 and an empty path.
        self._pre_order(root, 0, [], targetSum)
        return self.answer

    def _pre_order(
        self,
        node: Optional[TreeNode],
        sum_till_parent: int,
        path_till_parent: List[int],
        target_sum: int,
    ):
        """
        A private recursive helper method that performs a pre-order traversal (root, left, right)
        of the tree to find all paths that sum to the target.

        Args:
            node: The current node being visited.
            sum_till_parent: The sum of node values from the root to the current node's parent.
            path_till_parent: The list of nodes' values from the root to the current node's parent.
            target_sum: The target sum we are trying to achieve.
        """
        # We only proceed if the current node is not None.
        if node:
            # Calculate the current sum and update the path with the current node's value.
            current_sum = sum_till_parent + node.val
            path_till_parent.append(node.val)

            # Check if this is a leaf node and if the current path's sum matches the target.
            if node.left is None and node.right is None and current_sum == target_sum:
                # If it's a valid path, create a copy of the path and add it to the results.
                # We create a copy to avoid issues with the list being modified later in the recursion.
                self.answer.append(path_till_parent.copy())

            # Recurse on the left and right children.
            # We don't need a return value as we are collecting all valid paths in self.answer.
            if node.left:
                self._pre_order(node.left, current_sum, path_till_parent, target_sum)
            if node.right:
                self._pre_order(node.right, current_sum, path_till_parent, target_sum)

            # Backtrack: Remove the current node from the path list as we move up the tree.
            path_till_parent.pop()


class TestSolution(unittest.TestCase):
    """
    Unit tests for the Solution class.
    """

    def test_pathSum(self):
        """
        Tests the pathSum method with various tree configurations.
        """
        solution = Solution()

        # Test case 1: A tree with multiple valid paths.
        # Tree:      5
        #           / \
        #          4   8
        #         /   / \
        #        11  13  4
        #       / \     / \
        #      7   2   5   1
        root1 = TreeNode(5)
        root1.left = TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2)))
        root1.right = TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))

        # Paths that sum to 22: [5, 4, 11, 2] and [5, 8, 4, 5]
        expected_paths_1 = sorted([[5, 4, 11, 2], [5, 8, 4, 5]])
        actual_paths_1 = sorted(solution.pathSum(root1, 22))
        self.assertEqual(
            actual_paths_1,
            expected_paths_1,
            "Test Case 1 Failed: Should find both paths that sum to 22",
        )

        # Test case 2: Another valid path in the same tree.
        # Path that sums to 26: [5, 8, 13]
        self.assertEqual(
            sorted(solution.pathSum(root1, 26)),
            sorted([[5, 8, 13]]),
            "Test Case 2 Failed: Should find one path",
        )

        # Test case 3: A path that does not exist.
        self.assertEqual(
            solution.pathSum(root1, 30), [], "Test Case 3 Failed: Should find no paths"
        )

        # Test case 4: A single-node tree.
        root2 = TreeNode(1)
        self.assertEqual(
            solution.pathSum(root2, 1),
            [[1]],
            "Test Case 4 Failed: Should find a path with a single node",
        )
        self.assertEqual(
            solution.pathSum(root2, 0), [], "Test Case 4 Failed: Should find no paths"
        )

        # Test case 5: An empty tree.
        root3 = None
        self.assertEqual(
            solution.pathSum(root3, 0),
            [],
            "Test Case 5 Failed: Should find no paths for an empty tree",
        )

        # Test case 6: A tree with a valid path to a leaf, but no path to a non-leaf.
        # Tree:      1
        #           / \
        #          2   3
        root4 = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(
            sorted(solution.pathSum(root4, 3)),
            sorted([[1, 2]]),
            "Test Case 6 Failed: Should find path 1->2",
        )
        self.assertEqual(
            sorted(solution.pathSum(root4, 4)),
            sorted([[1, 3]]),
            "Test Case 6 Failed: Should find path 1->3",
        )
        self.assertEqual(
            solution.pathSum(root4, 5), [], "Test Case 6 Failed: Should not find any path"
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
