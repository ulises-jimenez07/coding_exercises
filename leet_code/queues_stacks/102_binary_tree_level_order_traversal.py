"""
Problem: Binary Tree Level Order Traversal - traverse tree level by level

Approach:
- Use BFS with a queue to process nodes level by level
- Track level size to group nodes at each depth
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(w) where w is max width of tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        """
        Performs a level-order traversal of a binary tree.
        Returns a list of lists, where each inner list represents a level.
        """
        if not root:
            return []

        queue = [root]
        ans = []

        while queue:
            level_size = len(queue)
            level = []

            for _ in range(level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            ans.append(level)

        return ans


import unittest


class TestLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test with an empty tree."""
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_single_node_tree(self):
        """Test with a single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.levelOrder(root), [[1]])

    def test_complete_binary_tree(self):
        """Test with a complete binary tree."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.levelOrder(root), [[3], [9, 20], [15, 7]])

    def test_incomplete_binary_tree(self):
        """Test with an incomplete binary tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        self.assertEqual(self.solution.levelOrder(root), [[1], [2, 3], [4]])

    def test_skewed_tree(self):
        """Test with a skewed tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.levelOrder(root), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
