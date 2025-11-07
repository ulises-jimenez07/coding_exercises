"""
Problem: Construct binary tree from preorder and inorder traversal arrays

Approach:
- Preorder first element is always root
- Find root in inorder to split left/right subtrees
- Use hashmap for O(1) inorder lookups
- Recursively build left and right subtrees
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(n) for hashmap and recursion
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0

        # Map inorder values to indices for O(1) lookup
        self.inorder_map = {}
        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i

        return self.helper_tree_builder(preorder, inorder, 0, len(inorder) - 1)

    def helper_tree_builder(self, preorder, inorder, inorder_start, inorder_end):
        if inorder_start > inorder_end:
            return None

        # Next element in preorder is root
        root_value = preorder[self.preorder_index]
        root = TreeNode(root_value)

        # Find root position in inorder
        root_index = self.inorder_map[root_value]

        self.preorder_index += 1

        # Build left then right subtrees
        root.left = self.helper_tree_builder(preorder, inorder, inorder_start, root_index - 1)
        root.right = self.helper_tree_builder(preorder, inorder, root_index + 1, inorder_end)

        return root


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def tree_to_list(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result

    def test_example_1(self):
        """Standard tree."""
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = [3, 9, 20, None, None, 15, 7]

        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)

    def test_single_node(self):
        """Single node tree."""
        preorder = [-1]
        inorder = [-1]
        expected = [-1]

        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)

    def test_empty_tree(self):
        """Empty tree."""
        preorder = []
        inorder = []

        result = self.solution.buildTree(preorder, inorder)
        self.assertIsNone(result)

    def test_left_skewed_tree(self):
        """Left-skewed tree."""
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        expected = [1, 2, None, 3]

        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)

    def test_right_skewed_tree(self):
        """Right-skewed tree."""
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        expected = [1, None, 2, None, 3]

        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)

    def test_larger_balanced_tree(self):
        """Larger balanced tree."""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]

        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
