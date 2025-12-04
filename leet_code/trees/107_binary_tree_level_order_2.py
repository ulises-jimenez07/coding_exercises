"""
Problem: Return level order traversal of binary tree in bottom-up order (leaf level first)

Approach:
- Use BFS with queue to traverse level by level
- Track level number with each node
- Group nodes by their level
- Reverse the result to get bottom-up order
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(w) where w is max width of tree
"""

import unittest
from collections import deque
from typing import (
    List,
    Optional,
)


class TreeNode:
    """Binary tree node with value and left/right children."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """BFS approach tracking level numbers with each node, reversed at end."""

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return bottom-up level order traversal of binary tree.
        """
        if not root:
            return []

        ans: list[list[int]] = []
        q: deque = deque()

        # Start with root at level 0
        q.append((root, 0))

        while q:
            curr_node, level = q.popleft()

            # Create new level list if needed
            if level == len(ans):
                ans.append([])

            # Add current node value to its level
            ans[level].append(curr_node.val)

            # Add children to queue with next level
            if curr_node.left:
                q.append((curr_node.left, level + 1))
            if curr_node.right:
                q.append((curr_node.right, level + 1))

        # Reverse to get bottom-up order
        return ans[::-1]


class Solution2:
    """Alternative approach: Process entire level at once, then reverse result."""

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Return bottom-up level order traversal using level-size approach.
        """
        if not root:
            return []

        queue: list = [root]
        ans: list[list[int]] = []

        while queue:
            # Capture number of nodes at current level
            level_size: int = len(queue)
            level: list[int] = []

            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add completed level to result
            ans.append(level)

        # Reverse to get bottom-up order
        return ans[::-1]


# -----------------------------------------------------------------------------


class TestLevelOrderBottom(unittest.TestCase):
    """Test cases for binary tree bottom-up level order traversal."""

    def setUp(self):
        """Initialize solution instance for each test."""
        self.solution = Solution()
        self.solution2 = Solution2()

    def _test_both_solutions(self, root, expected):
        """Helper method to test both solution implementations."""
        self.assertEqual(self.solution.levelOrderBottom(root), expected)
        self.assertEqual(self.solution2.levelOrderBottom(root), expected)

    def test_empty_tree(self):
        """Empty tree returns empty list."""
        self._test_both_solutions(None, [])

    def test_single_node_tree(self):
        """Single node tree returns single value in list."""
        root = TreeNode(1)
        self._test_both_solutions(root, [[1]])

    def test_full_binary_tree(self):
        """Complete binary tree with three levels."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected_output = [[15, 7], [9, 20], [3]]
        self._test_both_solutions(root, expected_output)

    def test_unbalanced_tree(self):
        """Unbalanced tree with right branch only."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        expected_output = [[3], [2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_tree_with_single_branch(self):
        """Left-skewed tree forms single branch."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected_output = [[3], [2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_balanced_tree_four_levels(self):
        """Balanced tree with four levels."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        root.left.left.left = TreeNode(8)
        expected_output = [[8], [4, 5, 6, 7], [2, 3], [1]]
        self._test_both_solutions(root, expected_output)

    def test_right_skewed_tree(self):
        """Right-skewed tree with only right children."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        root.right.right.right = TreeNode(4)
        expected_output = [[4], [3], [2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_tree_with_two_nodes_left(self):
        """Tree with root and left child only."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        expected_output = [[2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_tree_with_two_nodes_right(self):
        """Tree with root and right child only."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        expected_output = [[2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_tree_with_zigzag_pattern(self):
        """Tree with alternating left-right pattern."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.right = TreeNode(3)
        root.left.right.left = TreeNode(4)
        expected_output = [[4], [3], [2], [1]]
        self._test_both_solutions(root, expected_output)

    def test_larger_complete_tree(self):
        """Larger complete tree with multiple nodes per level."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        expected_output = [[4, 5, 6, 7], [2, 3], [1]]
        self._test_both_solutions(root, expected_output)

    def test_tree_with_negative_values(self):
        """Tree with negative node values."""
        root = TreeNode(-1)
        root.left = TreeNode(-2)
        root.right = TreeNode(-3)
        expected_output = [[-2, -3], [-1]]
        self._test_both_solutions(root, expected_output)


if __name__ == "__main__":
    unittest.main()
