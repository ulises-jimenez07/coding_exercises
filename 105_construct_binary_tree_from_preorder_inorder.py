from typing import List, Optional
import unittest


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
    
    Given two integer arrays preorder and inorder where preorder is the preorder 
    traversal of a binary tree and inorder is the inorder traversal of the same tree, 
    construct and return the binary tree.
    """
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Builds a binary tree from preorder and inorder traversal arrays.
        
        Algorithm:
        1. The first element in preorder is always the root
        2. Find the root's position in inorder to determine left and right subtrees
        3. Recursively build left and right subtrees
        
        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for the hashmap and recursion stack
        
        Args:
            preorder: List of integers representing preorder traversal
            inorder: List of integers representing inorder traversal
            
        Returns:
            TreeNode: Root of the constructed binary tree
        """
        # Index to track current position in preorder array
        self.preorder_index = 0
        
        # Map each value to its index in inorder array for O(1) lookup
        self.inorder_map = {}
        for i in range(len(inorder)):
            self.inorder_map[inorder[i]] = i

        return self.helper_tree_builder(preorder, inorder, 0, len(inorder) - 1)

    def helper_tree_builder(self, preorder, inorder, inorder_start, inorder_end):
        """
        Recursively builds the binary tree using divide and conquer approach.
        
        Args:
            preorder: Preorder traversal array
            inorder: Inorder traversal array
            inorder_start: Start index of current subtree in inorder array
            inorder_end: End index of current subtree in inorder array
            
        Returns:
            TreeNode: Root of the current subtree
        """
        # Base case: invalid range means no subtree exists
        if inorder_start > inorder_end:
            return None

        # Current root is the next element in preorder traversal
        root_value = preorder[self.preorder_index]
        root = TreeNode(root_value)

        # Find root's position in inorder array
        root_index = self.inorder_map[root_value]

        # Move to next element in preorder for next recursive call
        self.preorder_index += 1

        # Build left subtree first (preorder: root -> left -> right)
        # Left subtree elements are from inorder_start to root_index - 1
        root.left = self.helper_tree_builder(preorder, inorder, inorder_start, root_index - 1)
        
        # Build right subtree
        # Right subtree elements are from root_index + 1 to inorder_end
        root.right = self.helper_tree_builder(preorder, inorder, root_index + 1, inorder_end)

        return root


class TestSolution(unittest.TestCase):
    """Unit tests for the buildTree solution."""
    
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.solution = Solution()
    
    def tree_to_list(self, root):
        """Helper method to convert tree to list for easy comparison (level order)."""
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
    
    def test_example_1(self):
        """Test case 1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]"""
        preorder = [3, 9, 20, 15, 7]
        inorder = [9, 3, 15, 20, 7]
        expected = [3, 9, 20, None, None, 15, 7]
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)
    
    def test_single_node(self):
        """Test case 2: Single node tree"""
        preorder = [-1]
        inorder = [-1]
        expected = [-1]
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)
    
    def test_empty_tree(self):
        """Test case 3: Empty tree"""
        preorder = []
        inorder = []
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertIsNone(result)
    
    def test_left_skewed_tree(self):
        """Test case 4: Left-skewed tree"""
        preorder = [1, 2, 3]
        inorder = [3, 2, 1]
        expected = [1, 2, None, 3]
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)
    
    def test_right_skewed_tree(self):
        """Test case 5: Right-skewed tree"""
        preorder = [1, 2, 3]
        inorder = [1, 2, 3]
        expected = [1, None, 2, None, 3]
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)
    
    def test_larger_balanced_tree(self):
        """Test case 6: Larger balanced tree"""
        preorder = [1, 2, 4, 5, 3, 6, 7]
        inorder = [4, 2, 5, 1, 6, 3, 7]
        expected = [1, 2, 3, 4, 5, 6, 7]
        
        result = self.solution.buildTree(preorder, inorder)
        self.assertEqual(self.tree_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
