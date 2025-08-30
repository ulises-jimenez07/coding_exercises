import unittest
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Initializes a TreeNode with a value and optional left and right children.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree 'subRoot' is a subtree of another binary tree 'root'.

        A subtree of a tree is a tree that consists of a node in 'root' and all of its
        descendants. The structure and node values must match exactly.

        Args:
            root: The main binary tree.
            subRoot: The potential subtree.

        Returns:
            True if subRoot is a subtree of root, False otherwise.
        """
        # Base case: if the main tree is empty, it cannot contain any non-empty subtree.
        if not root:
            # If subRoot is also None, it's considered an empty subtree of an empty tree.
            # This is a common edge case to consider, though the subsequent checks handle it.
            return not subRoot

        # Check if the current node of 'root' and the 'subRoot' form the exact same tree.
        if self.is_same_tree(root, subRoot):
            return True

        # Recursively check if 'subRoot' is a subtree of the left or right child of 'root'.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        """
        Checks if two binary trees are structurally identical and have the same node values.

        Args:
            t1: The first binary tree.
            t2: The second binary tree.

        Returns:
            True if the trees are identical, False otherwise.
        """
        # Base case: If both trees are empty, they are the same.
        if not t1 and not t2:
            return True

        # If one tree is empty and the other is not, they are not the same.
        if not t1 or not t2:
            return False

        # If the values of the current nodes differ, they are not the same tree.
        if t1.val != t2.val:
            return False

        # Recursively check if the left subtrees and right subtrees are the same.
        return self.is_same_tree(t1.left, t2.left) and self.is_same_tree(t1.right, t2.right)

class TestIsSubtree(unittest.TestCase):
    """
    Unit tests for the Solution class's isSubtree method.
    """
    def test_basic_case(self):
        """
        Tests a simple case where the subtree exists.
        """
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        self.assertTrue(Solution().isSubtree(root, subRoot))

    def test_subtree_does_not_exist(self):
        """
        Tests a case where the subtree does not exist.
        """
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(3)) # Different right child
        self.assertFalse(Solution().isSubtree(root, subRoot))

    def test_empty_subroot(self):
        """
        Tests the edge case where the subRoot is None.
        An empty tree is considered a subtree of any non-empty tree.
        """
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        subRoot = None
        self.assertTrue(Solution().isSubtree(root, subRoot))

    def test_subroot_is_root(self):
        """
        Tests the case where the subRoot is the same as the main tree.
        """
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        self.assertTrue(Solution().isSubtree(root, subRoot))

    def test_empty_root(self):
        """
        Tests the case where the main root is None.
        An empty tree can only contain an empty subtree.
        """
        root = None
        subRoot = TreeNode(1)
        self.assertFalse(Solution().isSubtree(root, subRoot))

    def test_both_empty(self):
        """
        Tests the case where both root and subRoot are None.
        """
        root = None
        subRoot = None
        self.assertTrue(Solution().isSubtree(root, subRoot))

    def test_disjoint_trees(self):
        """
        Tests a case with two completely different trees.
        """
        root = TreeNode(1, TreeNode(2))
        subRoot = TreeNode(3, TreeNode(4))
        self.assertFalse(Solution().isSubtree(root, subRoot))

    def test_larger_but_not_matching(self):
        """
        Tests a case where a subtree has a larger value, which shouldn't match.
        """
        root = TreeNode(1, TreeNode(1, TreeNode(1, None, TreeNode(1)), TreeNode(1)), TreeNode(1, TreeNode(1)))
        # Change subRoot to a tree that is not a subtree of root.
        # For example, by changing a value or the structure.
        subRoot = TreeNode(1, None, TreeNode(2)) # A '2' in subRoot, but only '1's in root.
        self.assertFalse(Solution().isSubtree(root, subRoot))

if __name__ == '__main__':
    unittest.main()