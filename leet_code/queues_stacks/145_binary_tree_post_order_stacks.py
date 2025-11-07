"""
Problem: Binary Tree Postorder Traversal - visit left, right, then root using stacks

Approach:
- Use two stacks to simulate postorder without recursion
- First stack processes nodes, second reverses order
- Time complexity: O(n) where n is number of nodes
- Space complexity: O(h) where h is height of tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        """
        Performs a post-order traversal of a binary tree using two stacks.
        Visits nodes in the order: left subtree, right subtree, root.
        """
        ans = []
        if not root:
            return ans

        s1 = []
        s2 = []

        s1.append(root)
        while s1:
            x = s1.pop()
            s2.append(x)
            if x.left:
                s1.append(x.left)
            if x.right:
                s1.append(x.right)

        while s2:
            y = s2.pop()
            ans.append(y.val)

        return ans


import unittest


class TestPostorderTraversal(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_tree(self):
        """Test with an empty tree."""
        self.assertEqual(self.solution.postorderTraversal(None), [])

    def test_single_node(self):
        """Test with a single node tree."""
        root = TreeNode(1)
        self.assertEqual(self.solution.postorderTraversal(root), [1])

    def test_simple_tree(self):
        """Test with a simple tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [2, 3, 1])

    def test_complex_tree(self):
        """Test with a complex tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        self.assertEqual(self.solution.postorderTraversal(root), [4, 5, 2, 3, 1])

    def test_left_skewed_tree(self):
        """Test with a left-skewed tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])

    def test_right_skewed_tree(self):
        """Test with a right-skewed tree."""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(self.solution.postorderTraversal(root), [3, 2, 1])


if __name__ == "__main__":
    unittest.main()
