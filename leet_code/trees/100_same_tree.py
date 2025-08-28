import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    """
    A class to represent a node in a binary tree.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are the same.

        This method uses a recursive approach to compare the two trees.
        Two trees are considered the same if they are structurally identical
        and their nodes have the same values.

        Args:
            p: The root of the first binary tree.
            q: The root of the second binary tree.

        Returns:
            True if the trees are the same, False otherwise.
        """
        # Base case 1: Both nodes are None.
        # This means we've reached the end of a branch on both trees simultaneously,
        # which is a condition for structural similarity.
        if p is None and q is None:
            return True
        
        # Base case 2: One node is None and the other isn't.
        # This indicates a structural difference, so the trees are not the same.
        if p is None or q is None:
            return False

        # Recursive case: Both nodes are not None.
        # Check if the current nodes have the same value AND
        # recursively check if their left subtrees are the same AND
        # recursively check if their right subtrees are the same.
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# --------------------------------------------------------------------------------

class TestIsSameTree(unittest.TestCase):
    """
    Unit tests for the isSameTree method.
    """
    def test_same_trees(self):
        """
        Test case for two identical trees.
        """
        # Tree 1: [1, 2, 3]
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        # Tree 2: [1, 2, 3]
        q = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertTrue(Solution().isSameTree(p, q))

    def test_different_values(self):
        """
        Test case for trees with the same structure but different values.
        """
        # Tree 1: [1, 2, 3]
        p = TreeNode(1, TreeNode(2), TreeNode(3))
        # Tree 2: [1, 5, 3]
        q = TreeNode(1, TreeNode(5), TreeNode(3))
        self.assertFalse(Solution().isSameTree(p, q))

    def test_different_structure(self):
        """
        Test case for trees with different structures.
        """
        # Tree 1: [1, 2]
        p = TreeNode(1, TreeNode(2))
        # Tree 2: [1, null, 2]
        q = TreeNode(1, None, TreeNode(2))
        self.assertFalse(Solution().isSameTree(p, q))

    def test_empty_trees(self):
        """
        Test case for two empty trees (None roots).
        """
        self.assertTrue(Solution().isSameTree(None, None))

    def test_one_empty_tree(self):
        """
        Test case for one empty tree and one non-empty tree.
        """
        p = TreeNode(1)
        self.assertFalse(Solution().isSameTree(p, None))
        self.assertFalse(Solution().isSameTree(None, p))

if __name__ == '__main__':
    unittest.main()