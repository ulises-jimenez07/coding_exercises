import unittest
from typing import Optional, List, Deque
from collections import deque

# --- Binary Tree Node Definition ---
class TreeNode:
    """
    Definition for a binary tree node.
    Each node stores a value (val) and references to its left and right children.
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Solution Class ---
class Solution:
    """
    Contains the method to find the minimum depth of a binary tree.
    Minimum depth is the number of nodes along the shortest path 
    from the root node down to the nearest leaf node.
    """
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 'min_dept' (misspelled) is initialized but immediately overwritten by the function call.
        # This line is redundant in the current implementation:
        # min_dept = 0 


        # Recursive helper function to calculate the minimum depth.
        def min_depth(node: Optional[TreeNode]) -> int:
            # Base case: If the node is None (empty subtree), the depth is 0.
            if not node:
                return 0
            
            # Recursively find the minimum depth of the left and right subtrees.
            left_height = min_depth(node.left)
            right_height = min_depth(node.right)

            # Special case for minimum depth: A leaf node is a node with NO children.
            # If one child is missing (height == 0), the path MUST continue through the other child.
            
            # If the left subtree is empty, the min path must go through the right side.
            if left_height == 0:
                return right_height + 1 # +1 for the current node
            
            # If the right subtree is empty, the min path must go through the left side.
            if  right_height == 0:
                return left_height + 1          

            # Standard case: If both subtrees exist (non-zero height), 
            # the min depth is 1 (for the current node) plus the minimum of the two heights.
            return 1 + min(left_height, right_height)

        # Start the recursion from the root of the tree.
        return min_depth(root)

# --- Unit Test Class ---
class TestMinDepth(unittest.TestCase):
    """
    Test suite for the Solution.minDepth method.
    Includes a helper method to build a tree from a list (level-order representation).
    """

    def list_to_tree(self, arr: List[Optional[int]]) -> Optional[TreeNode]:
        """
        Converts a level-order list (with None for null nodes) to a binary tree.
        """
        if not arr or arr[0] is None:
            return None
        
        root = TreeNode(arr[0])
        queue: Deque[TreeNode] = deque([root])
        i = 1
        n = len(arr)
        
        while queue and i < n:
            current_node = queue.popleft()
            
            # Process left child
            if i < n and arr[i] is not None:
                current_node.left = TreeNode(arr[i])
                queue.append(current_node.left)
            i += 1
            
            # Process right child
            if i < n and arr[i] is not None:
                current_node.right = TreeNode(arr[i])
                queue.append(current_node.right)
            i += 1
            
        return root

    def test_basic_tree(self):
        # Tree: [3, 9, 20, None, None, 15, 7]
        # Min depth path: 3 -> 9 (depth 2)
        root = self.list_to_tree([3, 9, 20, None, None, 15, 7])
        expected_depth = 2
        self.assertEqual(Solution().minDepth(root), expected_depth)

    def test_single_node(self):
        # Tree: [1]
        # Min depth path: 1 (depth 1)
        root = self.list_to_tree([1])
        expected_depth = 1
        self.assertEqual(Solution().minDepth(root), expected_depth)

    def test_empty_tree(self):
        # Tree: [] (None root)
        # Min depth is 0
        root = self.list_to_tree([])
        expected_depth = 0
        self.assertEqual(Solution().minDepth(root), expected_depth)

    def test_skewed_tree_left(self):
        # Tree: [1, 2, None, 3, None, 4] -> 1 -> 2 -> 3 -> 4
        # Min depth path: 1 -> 2 -> 3 -> 4 (depth 4, as 4 is the only leaf)
        root = self.list_to_tree([1, 2, None, 3, None, None, None, 4])
        expected_depth = 3
        self.assertEqual(Solution().minDepth(root), expected_depth)

    def test_skewed_tree_right(self):
        # Tree: [1, None, 2, None, 3, None, 4] -> 1 -> 2 -> 3 -> 4
        # Min depth path: 1 -> 2 -> 3 -> 4 (depth 4, as 4 is the only leaf)
        root = self.list_to_tree([1, None, 2, None, None, None, 3, None, 4])
        expected_depth = 2
        self.assertEqual(Solution().minDepth(root), expected_depth)

    def test_complex_tree(self):
        # Tree: [2, None, 3, None, 4, None, 5, None, 6]
        # Min depth path: 2 -> 3 -> 4 -> 5 -> 6 (depth 5)
        root = self.list_to_tree([2, None, 3, None, 4, None, 5, None, 6])
        expected_depth = 5
        self.assertEqual(Solution().minDepth(root), expected_depth)

# This block allows the script to be executed and run the unit tests.
if __name__ == '__main__':
    # Running unittest.main with arguments prevents it from exiting the interpreter 
    # in environments like Jupyter/Colab/interactive shells.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)