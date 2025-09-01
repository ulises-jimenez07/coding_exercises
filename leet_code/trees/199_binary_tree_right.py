import unittest
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Contains methods to get the right side view of a binary tree.
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the rightmost node's value for each level of the binary tree
        using a standard BFS approach.

        This method uses a level-order traversal (Breadth-First Search)
        to visit nodes level by level. For each level, it identifies the
        last node visited, which is the rightmost node, and adds its value
        to the result list.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of integers representing the values of the nodes visible
            from the right side of the tree.
        """
        result = []
        if root is None:
            return result

        # Use a deque for efficient appends and pops from both ends.
        queue = deque([root])

        while queue:
            # Get the number of nodes at the current level.
            size = len(queue)

            # Iterate through all nodes at the current level.
            for i in range(size):
                node = queue.popleft()

                # Check if this is the last node of the current level.
                if i == size - 1:
                    result.append(node.val)

                # Add children to the queue for the next level's traversal.
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    def rightSideView_v2(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the rightmost node's value for each level of the binary tree
        using an alternative BFS approach.

        This version differs by collecting all nodes of a level into a
        separate list before appending the last one to the final result.
        It is less memory efficient than the first version as it stores
        all nodes of a level in an intermediate list.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of integers representing the values of the nodes visible
            from the right side of the tree.
        """
        if not root:
            return []

        queue = [root]  # Standard list can also act as a queue, but is less efficient for pop(0)
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

            ans.append(level[-1])

        return ans


# ------------------------------------------------------------------------------


class TestRightSideView(unittest.TestCase):
    """
    Unit tests for both versions of the rightSideView method.
    """

    def setUp(self):
        """
        Initializes the Solution class for each test.
        """
        self.solution = Solution()

    def test_example_tree(self):
        """
        Tests a standard example from LeetCode.
        Tree:
        """
        #      1
        #    /   \
        #   2     3
        #    \     \
        #     5     4
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)
        root.right.right = TreeNode(4)
        expected = [1, 3, 4]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_single_node(self):
        """
        Tests a tree with only one node.
        """
        root = TreeNode(1)
        expected = [1]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_empty_tree(self):
        """
        Tests an empty tree.
        """
        root = None
        expected = []
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_full_binary_tree(self):
        """
        Tests a full binary tree.
        Tree:
        """
        #      1
        #    /   \
        #   2     3
        #  / \   / \
        # 4   5 6   7
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        expected = [1, 3, 7]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_left_skewed_tree(self):
        """
        Tests a tree where all nodes are on the left side.
        Tree:
        """
        #      1
        #     /
        #    2
        #   /
        #  3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected = [1, 2, 3]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_right_skewed_tree(self):
        """
        Tests a tree where all nodes are on the right side.
        Tree:
        """
        #  1
        #   \
        #    2
        #     \
        #      3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        expected = [1, 2, 3]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)

    def test_complex_tree(self):
        """
        Tests a more complex tree structure.
        Tree:
        """
        #       10
        #      /  \
        #     5    15
        #    / \     \
        #   3   7    18
        #      /
        #     6
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.left.right.left = TreeNode(6)
        root.right.right = TreeNode(18)
        expected = [10, 15, 18, 6]
        self.assertEqual(self.solution.rightSideView(root), expected)
        self.assertEqual(self.solution.rightSideView_v2(root), expected)


if __name__ == "__main__":
    unittest.main()
