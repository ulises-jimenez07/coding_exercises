"""
Problem: Check if two nodes are cousins in a binary tree

Approach:
- Find depth and parent for both nodes
- Cousins have same depth but different parents
- Use DFS to locate each node and track parent/level
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height for recursion stack
"""

import unittest
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        x_info = self.find_node(root, x, None, 0)
        y_info = self.find_node(root, y, None, 0)

        if x_info and y_info:
            return x_info[0] != y_info[0] and x_info[1] == y_info[1]
        return False

    def find_node(self, node, val, parent, level):
        if not node:
            return None
        if node.val == val:
            return (parent, level)
        return self.find_node(node.left, val, node, level + 1) or self.find_node(node.right, val, node, level + 1)


class TestIsCousins(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_tree(self, values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        root = TreeNode(values[0])
        queue = [root]
        i = 1
        while i < len(values):
            current = queue.pop(0)
            if i < len(values) and values[i] is not None:
                current.left = TreeNode(values[i])
                queue.append(current.left)
            i += 1
            if i < len(values) and values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            i += 1
        return root

    def test_example_1(self):
        """Tests the first example case from LeetCode."""
        root = self.create_tree([1, 2, 3, 4])
        self.assertFalse(self.solution.isCousins(root, 4, 3))

    def test_example_2(self):
        """Tests the second example case from LeetCode."""
        root = self.create_tree([1, 2, 3, None, 4, None, 5])
        self.assertTrue(self.solution.isCousins(root, 5, 4))

    def test_example_3(self):
        """Tests the third example case from LeetCode."""
        root = self.create_tree([1, 2, 3, None, 4])
        self.assertFalse(self.solution.isCousins(root, 2, 3))

    def test_siblings(self):
        """Tests a case where the nodes are siblings."""
        root = self.create_tree([1, 2, 3, 4, 5])
        self.assertFalse(self.solution.isCousins(root, 4, 5))

    def test_cousins_at_level_2(self):
        """Tests a case where the nodes are cousins at level 2."""
        root = self.create_tree([1, 2, 3, 4, 5, 6, 7])
        self.assertTrue(self.solution.isCousins(root, 4, 6))

    def test_nodes_not_in_tree(self):
        """Tests a case where one or both nodes are not in the tree."""
        root = self.create_tree([1, 2, 3])
        self.assertFalse(self.solution.isCousins(root, 4, 5))


if __name__ == "__main__":
    unittest.main()
