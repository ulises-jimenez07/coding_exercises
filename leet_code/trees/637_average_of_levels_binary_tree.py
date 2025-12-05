"""
Problem: Return the average value of the nodes on each level of the binary tree.

Approach:
- Use BFS (Breadth-First Search) with a queue to traverse level by level.
- For each level, process all nodes currently in the queue.
- Calculate the sum of the node values and the count of nodes for the current level.
- Divide the sum by the count to get the average, and store it.
- Time complexity: O(n) where n is the number of nodes, as each node is visited once.
- Space complexity: O(w) where w is the maximum width of the tree (max number of nodes in a level).
"""

import unittest
from collections import deque
from typing import (
    List,
    Optional,
)


# Definition for a binary tree node.
class TreeNode:
    """Binary tree node with value and left/right children."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    BFS approach to calculate the average of node values for each level.
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Calculates the average of node values for each level of the binary tree.
        """
        # Handle edge case for an empty tree
        if not root:
            return []

        # List to store the average of each level
        ans = []
        # Queue for BFS, initialized with the root node
        queue: deque[TreeNode] = deque()
        queue.append(root)

        # Process the tree level by level
        while queue:
            # Get the number of nodes at the current level
            level_size = len(queue)
            level_sum = 0

            # Process all nodes at the current level
            for _ in range(level_size):
                # Dequeue the current node
                curr_node = queue.popleft()
                # Accumulate the sum of values
                level_sum += curr_node.val

                # Enqueue the left child for the next level
                if curr_node.left:
                    queue.append(curr_node.left)
                # Enqueue the right child for the next level
                if curr_node.right:
                    queue.append(curr_node.right)

            # Calculate and store the average for the current level
            ans.append(level_sum / level_size)

        return ans


# -----------------------------------------------------------------------------


class TestAverageOfLevels(unittest.TestCase):
    """Test cases for averageOfLevels method."""

    def setUp(self):
        """Initialize solution instance for each test."""
        self.solution = Solution()

    def test_empty_tree(self):
        """Empty tree returns empty list."""
        self.assertEqual(self.solution.averageOfLevels(None), [])

    def test_single_node_tree(self):
        """Single node tree returns single value in list."""
        root = TreeNode(5)
        self.assertEqual(self.solution.averageOfLevels(root), [5.0])

    def test_example_tree(self):
        """Test with the tree from the problem description example."""
        # Tree: [3, 9, 20, null, null, 15, 7]
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        # Level 0: [3] -> 3.0
        # Level 1: [9, 20] -> 14.5
        # Level 2: [15, 7] -> 11.0
        expected_output = [3.0, 14.5, 11.0]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)

    def test_another_example_tree(self):
        """Test with a different tree structure."""
        # Tree: [2, 1, 3, 0, 7, 9, 1, 2, null, 1, 0, null, null, 8, 8, null, null, null, null, null, null, null, null]
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(1)
        root.left.left.left = TreeNode(2)
        root.left.right.left = TreeNode(1)
        root.left.right.right = TreeNode(0)
        root.right.right.left = TreeNode(8)
        root.right.right.right = TreeNode(8)

        # Level 0: [2] -> 2.0
        # Level 1: [1, 3] -> (1+3)/2 = 2.0
        # Level 2: [0, 7, 9, 1] -> (0+7+9+1)/4 = 17/4 = 4.25
        # Level 3: [2, 1, 0, 8, 8] -> (2+1+0+8+8)/5 = 19/5 = 3.8
        expected_output = [2.0, 2.0, 4.25, 3.8]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)

    def test_unbalanced_tree_left(self):
        """Unbalanced tree with only left children."""
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.left.left = TreeNode(1)
        # Level 0: [10] -> 10.0
        # Level 1: [5] -> 5.0
        # Level 2: [1] -> 1.0
        expected_output = [10.0, 5.0, 1.0]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)

    def test_unbalanced_tree_right(self):
        """Unbalanced tree with only right children."""
        root = TreeNode(10)
        root.right = TreeNode(20)
        root.right.right = TreeNode(30)
        # Level 0: [10] -> 10.0
        # Level 1: [20] -> 20.0
        # Level 2: [30] -> 30.0
        expected_output = [10.0, 20.0, 30.0]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)

    def test_full_tree_with_negatives(self):
        """Full binary tree including negative values."""
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        root.left.left = TreeNode(-4)
        root.left.right = TreeNode(-5)
        root.right.left = TreeNode(-6)
        root.right.right = TreeNode(-7)
        # Level 0: [-1] -> -1.0
        # Level 1: [-2, -3] -> (-2 + -3)/2 = -2.5
        # Level 2: [-4, -5, -6, -7] -> (-4 + -5 + -6 + -7)/4 = -22/4 = -5.5
        expected_output = [-1.0, -2.5, -5.5]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)

    def test_tree_with_zeros(self):
        """Tree including zero values."""
        root = TreeNode(0)
        root.left = TreeNode(0)
        root.right = TreeNode(0)
        root.left.right = TreeNode(10)
        # Level 0: [0] -> 0.0
        # Level 1: [0, 0] -> 0.0
        # Level 2: [10] -> 10.0
        expected_output = [0.0, 0.0, 10.0]
        self.assertEqual(self.solution.averageOfLevels(root), expected_output)


if __name__ == "__main__":
    unittest.main()
