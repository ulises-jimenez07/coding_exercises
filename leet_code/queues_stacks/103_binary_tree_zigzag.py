"""
Problem: Binary Tree Zigzag Level Order Traversal - alternate direction per level

Approach:
- Use BFS with a queue and reverse alternate levels
- Track level index to determine when to reverse
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
    def zigzagLevelOrder(self, root):
        """
        Performs a zigzag level-order traversal of a binary tree.
        Alternates between left-to-right and right-to-left traversal for each level.
        """
        if not root:
            return []

        ans = []
        q = [root]
        level_index = 1

        while q:
            level = []
            q_len = len(q)

            for _ in range(q_len):
                current = q.pop(0)
                level.append(current.val)

                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)

            if level_index % 2 == 0:
                ans.append(level[::-1])
            else:
                ans.append(level)

            level_index += 1

        return ans


import unittest


class TestZigzagLevelOrder(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test with an empty tree."""
        self.assertEqual(self.solution.zigzagLevelOrder(None), [])

    def test_single_node(self):
        """Test with a single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1]])

    def test_simple_tree(self):
        """Test with a simple tree."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[3], [20, 9]])

    def test_complex_tree(self):
        """Test with a complex tree."""
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[3], [20, 9], [15, 7]])

    def test_left_skewed_tree(self):
        """Test with a left-skewed tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [2], [3]])

    def test_right_skewed_tree(self):
        """Test with a right-skewed tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.zigzagLevelOrder(root), [[1], [2], [3]])


if __name__ == "__main__":
    unittest.main()
