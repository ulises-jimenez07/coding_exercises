"""
Problem: Return level order traversal of binary tree (nodes at each level grouped)

Approach:
- Use BFS with queue to traverse level by level
- Track level number with each node
- Group nodes by their level
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(w) where w is max width
"""

import unittest
from collections import deque
from typing import (
    List,
    Optional,
)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([(root, 1)])
        answer: list[list[int]] = []

        while q:
            (node, level) = q.popleft()

            # Create new level list if needed
            if len(answer) < level:
                answer.append([])

            answer[level - 1].append(node.val)

            # Add children to queue with next level
            if node.left:
                q.append((node.left, level + 1))

            if node.right:
                q.append((node.right, level + 1))

        return answer


# -----------------------------------------------------------------------------


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Empty tree."""
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_single_node_tree(self):
        """Single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.levelOrder(root), [[1]])

    def test_full_binary_tree(self):
        """Complete binary tree."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected_output = [[3], [9, 20], [15, 7]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)

    def test_unbalanced_tree(self):
        """Unbalanced tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        expected_output = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)

    def test_tree_with_single_branch(self):
        """Left-skewed tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected_output = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)


if __name__ == "__main__":
    unittest.main()
