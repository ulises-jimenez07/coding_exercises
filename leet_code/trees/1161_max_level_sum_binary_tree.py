# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
import unittest
from typing import Optional


class TreeNode:
    """A node in a binary tree."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class to find the level with the maximum sum in a binary tree.
    """

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        Calculates the level with the maximum sum in a binary tree.

        This method uses a breadth-first search (BFS) approach with a queue to
        traverse the tree level by level. It maintains a dictionary to store
        the sum of node values for each level. After traversing the entire tree,
        it iterates through the dictionary to find the level with the highest sum.

        Args:
            root: The root node of the binary tree.

        Returns:
            The level number (1-indexed) with the maximum sum.
        """
        if not root:
            return 0  # Return 0 or handle as per problem constraints for an empty tree

        # Dictionary to store the sum of values for each level.
        sum_per_level = {}
        # A deque for a breadth-first traversal, storing tuples of (level, node).
        q = deque([(1, root)])

        while q:
            level, node = q.popleft()

            # Add the current node's value to its corresponding level's sum.
            # If the level is not yet in the dictionary, initialize its sum to 0.
            sum_per_level.setdefault(level, 0)
            sum_per_level[level] += node.val

            # Enqueue the children for the next level if they exist.
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))

        # Find the level with the maximum sum.
        # Initialize `ans` with the first level in the dictionary.
        ans = 1
        # Iterate through the dictionary keys (levels) to find the one with the max sum.
        for level in sum_per_level:
            if sum_per_level[level] > sum_per_level[ans]:
                ans = level

        return ans


# --- Unit Tests ---


class TestMaxLevelSum(unittest.TestCase):
    """
    Unit tests for the maxLevelSum method.
    """

    def setUp(self):
        """
        Set up a new Solution object for each test.
        """
        self.solution = Solution()

    def test_example_tree(self):
        """
        Test case from the LeetCode example.
        Tree: [1,7,0,7,-8,None,None]
        Level 1: 1
        Level 2: 7 + 0 = 7
        Level 3: 7 + -8 = -1
        Max sum is 7 at level 2.
        """
        root = TreeNode(1)
        root.left = TreeNode(7)
        root.right = TreeNode(0)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(-8)
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_single_node(self):
        """
        Test a tree with only one node.
        """
        root = TreeNode(10)
        self.assertEqual(self.solution.maxLevelSum(root), 1)

    def test_empty_tree(self):
        """
        Test an empty tree (root is None).
        The function should handle this gracefully.
        """
        self.assertEqual(self.solution.maxLevelSum(None), 0)

    def test_all_negative_values(self):
        """
        Test a tree with all negative values.
        """
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(-4)
        self.assertEqual(
            self.solution.maxLevelSum(root), 1
        )  # Level 1 sum is -1, Level 2 is -5, Level 3 is -4

    def test_multiple_levels_with_same_max_sum(self):
        """
        Test a tree where multiple levels have the same maximum sum.
        The function should return the smallest level number.
        Tree: [1, 2, 0, None, None, 1, 1]
        Level 1: 1
        Level 2: 2 + 0 = 2
        Level 3: 1 + 1 = 2
        Max sum is 2 at levels 2 and 3. The function should return 2.
        """
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(0)
        root.right.left = TreeNode(1)
        root.right.right = TreeNode(1)
        self.assertEqual(self.solution.maxLevelSum(root), 2)

    def test_imbalanced_tree(self):
        """
        Test an imbalanced tree.
        Tree: [1, -2, None, 3, None, -4]
        Level 1: 1
        Level 2: -2
        Level 3: 3
        Level 4: -4
        Max sum is 3 at level 3.
        """
        root = TreeNode(1)
        root.left = TreeNode(-2)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(-4)
        self.assertEqual(self.solution.maxLevelSum(root), 3)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
