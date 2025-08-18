from typing import Optional, List
import unittest


# Definition for a binary tree node.
# The TreeNode class represents a node in a binary tree.
# It holds the node's value and references to its left and right children.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal of a binary tree.

        Inorder traversal visits nodes in the order: left subtree -> root -> right subtree.
        This recursive approach uses a helper function and a class attribute to
        store the result.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of integers representing the inorder traversal of the tree.
        """
        self.ans = []  # Initialize an empty list to store the traversal results
        self._inorder(root)  # Start the recursive traversal from the root
        return self.ans

    def _inorder(self, node: Optional[TreeNode]):
        """
        A private recursive helper function to perform the inorder traversal.

        Args:
            node: The current node being visited.
        """
        if node:
            self._inorder(node.left)  # Traverse the left subtree
            self.ans.append(node.val)  # Visit the root node
            self._inorder(node.right)  # Traverse the right subtree


# --- Unit Tests ---
class TestInorderTraversal(unittest.TestCase):
    """
    Unit tests for the inorderTraversal method.
    """

    def test_empty_tree(self):
        """Test with an empty tree (root is None)."""
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(None), [])

    def test_single_node_tree(self):
        """Test with a tree containing a single node."""
        root = TreeNode(10)
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [10])

    def test_simple_tree(self):
        """
        Test a simple tree with a left and right child.
        
        Tree structure:
             2
            / \\
           1   3
        """
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [1, 2, 3])

    def test_complex_tree(self):
        """
        Test a more complex tree with multiple levels and branches.
        
        Tree structure:
                 10
                /  \\
               5    15
              / \\     \\
             3   7     20
        """
        root = TreeNode(
            10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(20))
        )
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [3, 5, 7, 10, 15, 20])

    def test_skewed_left_tree(self):
        """
        Test a tree where all nodes are to the left.

        Tree structure:
               5
              /
             4
            /
           3
        """
        root = TreeNode(5, TreeNode(4, TreeNode(3)))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [3, 4, 5])

    def test_skewed_right_tree(self):
        """
        Test a tree where all nodes are to the right.
        
        Tree structure:
             1
              \\
               2
                \\
                 3
        """
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        sol = Solution()
        self.assertEqual(sol.inorderTraversal(root), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
