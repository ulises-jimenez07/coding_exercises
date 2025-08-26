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
    """
    A class to determine if two nodes in a binary tree are cousins.
    Cousins are nodes that are at the same level but have different parents.
    """

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        """
        Determines if nodes with values x and y are cousins.

        Args:
            root: The root node of the binary tree.
            x: The value of the first node to check.
            y: The value of the second node to check.

        Returns:
            True if x and y are cousins, False otherwise.
        """
        # Instance variables to store the parent and level of the target nodes.
        self.first_parent = None
        self.second_parent = None
        self.first_level = -1
        self.second_level = -1

        # Perform a pre-order traversal to find the parent and level of x and y.
        self._pre_order(root, 0, None, x, y)

        # Cousins must have different parents and be at the same level.
        return self.first_parent != self.second_parent and self.first_level == self.second_level

    def _pre_order(self, node, level, parent, x, y):
        """
        A recursive helper function for pre-order traversal.

        Args:
            node: The current node being visited.
            level: The current depth of the node.
            parent: The parent node of the current node.
            x: The value of the first node to find.
            y: The value of the second node to find.
        """
        # Base case: if the node is None, stop the recursion.
        if not node:
            return

        # Check if the current node's value matches x or y.
        if node.val == x:
            self.first_parent = parent
            self.first_level = level
        if node.val == y:
            self.second_parent = parent
            self.second_level = level

        # Recursively traverse the left and right subtrees.
        self._pre_order(node.left, level + 1, node, x, y)
        self._pre_order(node.right, level + 1, node, x, y)


# -----------------------------------------------------------------------------


class TestIsCousins(unittest.TestCase):
    """
    Unit tests for the isCousins method.
    """

    def setUp(self):
        """
        Set up the Solution object before each test.
        """
        self.solution = Solution()

    def test_example_1(self):
        """
        Test case from LeetCode example 1.
        Tree: [1,2,3,4], x=4, y=3
        Expected: False (different levels)
        """
        root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 4, 3))

    def test_example_2(self):
        """
        Test case from LeetCode example 2.
        Tree: [1,2,3,null,4,null,5], x=5, y=4
        Expected: True (same level, different parents)
        """
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3, None, TreeNode(5)))
        self.assertTrue(self.solution.isCousins(root, 5, 4))

    def test_example_3(self):
        """
        Test case from LeetCode example 3.
        Tree: [1,2,3,null,4], x=2, y=3
        Expected: False (same parents)
        """
        root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 2, 3))

    def test_siblings(self):
        """
        Test case where nodes are siblings (same parent, same level).
        Tree: [1,2,3,4,5], x=4, y=5
        Expected: False (same parent)
        """
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 4, 5))

    def test_cousins_at_level_2(self):
        """
        Test case for two nodes at the same level with different parents.
        Tree: [1,2,3,4,5,6,7], x=5, y=7
        Expected: True
        """
        root = TreeNode(
            1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))
        )
        self.assertTrue(self.solution.isCousins(root, 5, 7))

    def test_x_is_root(self):
        """
        Test case where one of the nodes is the root.
        Expected: False, as root has no parent and thus cannot be a cousin.
        """
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 1, 2))

    def test_y_is_root(self):
        """
        Test case where one of the nodes is the root.
        Expected: False, as root has no parent and thus cannot be a cousin.
        """
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 2, 1))

    def test_nodes_not_in_tree(self):
        """
        Test case where one or both nodes are not in the tree.
        Expected: False, as their level will remain at -1.
        """
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertFalse(self.solution.isCousins(root, 4, 5))
        self.assertFalse(self.solution.isCousins(root, 2, 5))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
