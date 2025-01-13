# Definition for a binary tree node.
from collections import defaultdict, deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Performs a vertical traversal of a binary tree.

        Args:
            root: The root of the binary tree.

        Returns:
            A list of lists, where each inner list contains the node values at a specific vertical column,
            ordered from leftmost column to rightmost column.  Nodes within the same column are ordered from top to bottom.
        """
        if not root:
            return []  # Empty tree, return empty list

        queue = deque([(root, 0)])  # Initialize queue with root and its column (0)
        column_hash = defaultdict(list)  # Store nodes by column

        while queue:
            curr, column = queue.popleft()  # Process node and its column
            column_hash[column].append(curr.val)  # Add node value to its column's list
            if curr.left:
                queue.append(
                    (curr.left, column - 1)
                )  # Add left child to queue, decrement column
            if curr.right:
                queue.append(
                    (curr.right, column + 1)
                )  # Add right child to queue, increment column

        return [
            column_hash[x] for x in sorted(column_hash.keys())
        ]  # Return lists of node values, sorted by column


import unittest


class TestVerticalOrder(unittest.TestCase):
    def test_vertical_order(self):
        solution = Solution()

        # Test case 1: Example 1
        root1 = TreeNode(3)
        root1.left = TreeNode(9)
        root1.right = TreeNode(20)
        root1.right.left = TreeNode(15)
        root1.right.right = TreeNode(7)
        self.assertEqual(solution.verticalOrder(root1), [[9], [3, 15], [20], [7]])

        # Test case 2: Example 2
        root2 = TreeNode(1)
        root2.left = TreeNode(2)
        root2.left.left = TreeNode(4)
        root2.left.right = TreeNode(5)
        root2.right = TreeNode(3)
        root2.right.left = TreeNode(6)
        root2.right.right = TreeNode(7)

        self.assertEqual(solution.verticalOrder(root2), [[4], [2], [1, 5, 6], [3], [7]])

        # Test case 3: Empty tree
        self.assertEqual(solution.verticalOrder(None), [])

        # Test case 4: Single node tree
        root4 = TreeNode(1)
        self.assertEqual(solution.verticalOrder(root4), [[1]])

        # Test case 5: Skewed left tree
        root5 = TreeNode(1)
        root5.left = TreeNode(2)
        root5.left.left = TreeNode(3)
        self.assertEqual(solution.verticalOrder(root5), [[3], [2], [1]])


if __name__ == "__main__":
    unittest.main()
