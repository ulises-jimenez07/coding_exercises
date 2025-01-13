from typing import Optional, List
import unittest


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
        Given the root of a binary tree, return all root-to-leaf paths in any order.

        A leaf is a node with no children.

        Args:
            root: The root of the binary tree.

        Returns:
            A list of strings representing the root-to-leaf paths.
        """

        def construct_paths(root, path):
            """
            Recursively constructs the paths from the given node.

            Args:
                root: The current node.
                path: The current path string.
            """
            if root is None:
                return

            path += str(root.val)  # Add the current node's value to the path

            if root.left is None and root.right is None:
                paths.append(path)  # If it's a leaf node, add the path to the result
            else:
                path += "->"  # If not a leaf, add the separator
                construct_paths(root.left, path)  # Explore the left subtree
                construct_paths(root.right, path)  # Explore the right subtree

        paths = []
        construct_paths(root, "")
        return paths


class TestBinaryTreePaths(unittest.TestCase):
    def test_empty_tree(self):
        """Test case for an empty tree."""
        solution = Solution()
        self.assertEqual(solution.binaryTreePaths(None), [])

    def test_single_node(self):
        """Test case for a tree with a single node."""
        root = TreeNode(1)
        solution = Solution()
        self.assertEqual(solution.binaryTreePaths(root), ["1"])

    def test_simple_tree(self):
        """Test case for a simple tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(sorted(solution.binaryTreePaths(root)), sorted(["1->2", "1->3"]))

    def test_complex_tree(self):
        """Test case for a more complex tree."""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        solution = Solution()
        self.assertEqual(sorted(solution.binaryTreePaths(root)), sorted(["1->2->5", "1->3"]))

    def test_skewed_left_tree(self):
        """Test case for a skewed left tree"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.binaryTreePaths(root), ["1->2->3"])

    def test_skewed_right_tree(self):
        """Test case for a skewed right tree"""
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        solution = Solution()
        self.assertEqual(solution.binaryTreePaths(root), ["1->2->3"])


if __name__ == "__main__":
    unittest.main()
