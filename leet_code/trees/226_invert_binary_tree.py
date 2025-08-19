import unittest
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Main function to initiate the inversion process.
        It calls the recursive helper method `invert`.

        Args:
            root: The root node of the binary tree.

        Returns:
            The root node of the inverted binary tree.
        """
        return self.invert(root)

    def invert(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Recursively inverts a binary tree.

        The base case is when the node is None, in which case it returns None.
        Otherwise, it recursively calls itself on the left and right children,
        then swaps the left and right children of the current node.

        Args:
            node: The current node to invert.

        Returns:
            The inverted node.
        """
        # Base case: if the node is None, return it
        if not node:
            return None

        # Recursively invert the left and right subtrees
        left_inverted = self.invert(node.left)
        right_inverted = self.invert(node.right)

        # Swap the left and right children of the current node
        node.left = right_inverted
        node.right = left_inverted

        # Return the inverted node
        return node


# Helper function to create a tree from a list (for testing)
def create_tree(nodes: list[Optional[int]]) -> Optional[TreeNode]:
    """Creates a binary tree from a list of values in level-order."""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current_node = queue.pop(0)

        if nodes[i] is not None:
            current_node.left = TreeNode(nodes[i])
            queue.append(current_node.left)
        i += 1

        if i < len(nodes) and nodes[i] is not None:
            current_node.right = TreeNode(nodes[i])
            queue.append(current_node.right)
        i += 1
    return root


# Helper function to serialize a tree to a list (for testing)
def serialize_tree(root: Optional[TreeNode]) -> list[Optional[int]]:
    """Serializes a binary tree to a list of values in level-order."""
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

    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()

    return result


class TestInvertTree(unittest.TestCase):
    """
    Unit tests for the invertTree method.
    """

    def test_example_case(self):
        """
        Tests the example from the problem description:
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
        """
        solution = Solution()
        root = create_tree([4, 2, 7, 1, 3, 6, 9])
        inverted_root = solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [4, 7, 2, 9, 6, 3, 1])

    def test_empty_tree(self):
        """
        Tests the case with an empty tree.
        Input: root = []
        Output: []
        """
        solution = Solution()
        root = create_tree([])
        inverted_root = solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [])

    def test_single_node_tree(self):
        """
        Tests the case with a single-node tree.
        Input: root = [1]
        Output: [1]
        """
        solution = Solution()
        root = create_tree([1])
        inverted_root = solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [1])

    def test_unbalanced_tree(self):
        """
        Tests a case with an unbalanced tree.
        Input: root = [1, 2]
        Output: [1, None, 2]
        """
        solution = Solution()
        root = create_tree([1, 2])
        inverted_root = solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [1, None, 2])

    def test_complex_tree(self):
        """
        Tests a more complex, multi-level tree.
        Input: root = [10, 5, 15, 2, 7, 12, 17]
        Output: [10, 15, 5, 17, 12, 7, 2]
        """
        solution = Solution()
        root = create_tree([10, 5, 15, 2, 7, 12, 17])
        inverted_root = solution.invertTree(root)
        self.assertEqual(serialize_tree(inverted_root), [10, 15, 5, 17, 12, 7, 2])


# Run the tests
if __name__ == "__main__":
    unittest.main()
