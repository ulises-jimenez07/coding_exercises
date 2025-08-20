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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        """
        Calculates the diameter of a binary tree. The diameter is the length
        of the longest path between any two nodes in a tree. This path may or may not
        pass through the root.

        Args:
            root: The root node of the binary tree.

        Returns:
            The diameter of the binary tree.
        """
        # A nonlocal variable to store the maximum diameter found so far.
        diameter = 0

        def longest_path(node):
            """
            A helper function to recursively find the longest path (height) from a given node
            to its furthest leaf. It also updates the global diameter.

            Args:
                node: The current node in the traversal.

            Returns:
                The height of the subtree rooted at the current node.
            """
            # Base case: if the node is None, it means we've gone past a leaf,
            # so we return -1 to represent a path of length 0 from a leaf.
            if not node:
                return -1

            # Use nonlocal to modify the 'diameter' variable defined in the outer scope.
            nonlocal diameter

            # Recursively find the height of the left and right subtrees.
            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            # The diameter through the current node is the sum of the heights of its
            # left and right subtrees plus 2 (for the two edges connecting the node).
            # We update the global diameter with the maximum value found.
            diameter = max(diameter, left_path + right_path + 2)

            # The height of the current subtree is 1 (for the edge to the node's parent)
            # plus the maximum of the heights of its left and right subtrees.
            return max(left_path, right_path) + 1

        # Start the recursive traversal from the root.
        longest_path(root)

        # Return the maximum diameter found during the traversal.
        return diameter


# Unit tests
import unittest


class TestSolution(unittest.TestCase):
    """
    Unit tests for the diameterOfBinaryTree method.
    """

    def test_simple_tree(self):
        """
        Test a simple binary tree.

        """
        # Create a simple tree:
        #      1
        #     / \
        #    2   3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        self.assertEqual(Solution().diameterOfBinaryTree(root), 2)

    def test_long_tree(self):
        """
        Test a tree with a long path.

        """
        # Create a tree with a long path on the left side:
        #        1
        #       / \
        #      2   3
        #     / \
        #    4   5
        #   / \
        #  6   7
        root = TreeNode(
            1, TreeNode(2, TreeNode(4, TreeNode(6), TreeNode(7)), TreeNode(5)), TreeNode(3)
        )
        self.assertEqual(Solution().diameterOfBinaryTree(root), 4)

    def test_skewed_tree(self):
        """
        Test a skewed tree.

        """
        # Create a skewed tree (all nodes on one side):
        # 1
        #  \
        #   2
        #    \
        #     3
        #      \
        #       4
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        self.assertEqual(Solution().diameterOfBinaryTree(root), 3)

    def test_single_node_tree(self):
        """
        Test a tree with only one node.
        """
        root = TreeNode(1)
        self.assertEqual(Solution().diameterOfBinaryTree(root), 0)

    def test_empty_tree(self):
        """
        Test an empty tree.
        """
        root = None
        self.assertEqual(Solution().diameterOfBinaryTree(root), 0)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
