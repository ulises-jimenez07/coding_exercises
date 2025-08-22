from collections import deque
import unittest
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
    A class containing methods to solve binary tree problems.
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a level-order traversal of a binary tree.

        This method uses a breadth-first search (BFS) approach with a deque to
        traverse the tree level by level. It stores the nodes along with their
        respective levels to group the values correctly in the final output.

        Args:
            root: The root node of the binary tree.

        Returns:
            A list of lists, where each inner list contains the values of the
            nodes at the same level.
        """
        # If the root is None, the tree is empty, so return an empty list.
        if root is None:
            return []

        # Use a deque for efficient appends and pops from both ends.
        # Each element in the deque is a tuple: (node, level).
        q = deque([(root, 1)])
        answer = []

        # Process nodes until the queue is empty.
        while q:
            # Pop the first element (node and its level) from the left of the queue.
            (node, level) = q.popleft()

            # If the current level hasn't been added to the answer list yet,
            # create a new sublist for it.
            if len(answer) < level:
                answer.append([])

            # Append the current node's value to the list corresponding to its level.
            answer[level - 1].append(node.val)

            # If the current node has a left child, add it to the queue with the next level.
            if node.left:
                q.append((node.left, level + 1))

            # If the current node has a right child, add it to the queue with the next level.
            if node.right:
                q.append((node.right, level + 1))

        return answer


# -----------------------------------------------------------------------------

## Unit Tests


class TestLevelOrder(unittest.TestCase):
    """
    Unit tests for the levelOrder method of the Solution class.
    """

    def setUp(self):
        """
        Sets up a new instance of the Solution class for each test.
        """
        self.solution = Solution()

    def test_empty_tree(self):
        """
        Test case for an empty tree (root is None).
        """
        self.assertEqual(self.solution.levelOrder(None), [])

    def test_single_node_tree(self):
        """
        Test case for a tree with a single node.
        """
        root = TreeNode(1)
        self.assertEqual(self.solution.levelOrder(root), [[1]])

    def test_full_binary_tree(self):
        """
        Test case for a complete binary tree.
        """
        # Tree structure:
        #      3
        #     / \
        #    9  20
        #      /  \
        #     15   7
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        expected_output = [[3], [9, 20], [15, 7]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)

    def test_unbalanced_tree(self):
        """
        Test case for an unbalanced tree.
        """
        # Tree structure:
        #     1
        #      \
        #       2
        #      /
        #     3
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)
        expected_output = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)

    def test_tree_with_single_branch(self):
        """
        Test case for a tree that is essentially a linked list.
        """
        # Tree structure:
        #     1
        #    /
        #   2
        #  /
        # 3
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        expected_output = [[1], [2], [3]]
        self.assertEqual(self.solution.levelOrder(root), expected_output)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
