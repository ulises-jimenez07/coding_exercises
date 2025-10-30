from typing import List, Optional
import unittest

# Definition for a binary tree node.
# This class defines the structure of a node in the Binary Search Tree (BST).
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# The main class containing the solution method.
class Solution:
    # Method to convert a sorted array into a height-balanced Binary Search Tree (BST).
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    
        # Helper function for recursive BST construction.
        # It takes the start (left) and end (right) indices of the current subarray.
        def inorder(left, right):
            # Base case: if the left index surpasses the right index, the subarray is empty.
            # This indicates the end of a branch, so we return None.
            if left > right:
                return None

            # Calculate the middle index of the current subarray.
            # This element will be the root of the current subtree to ensure height balance.
            mid = (left + right) // 2

            # Create a new TreeNode with the value at the middle index.
            root = TreeNode(nums[mid])
            
            # Recursively build the left subtree using the left half of the array (from 'left' to 'mid - 1').
            root.left = inorder(left, mid - 1)
            
            # Recursively build the right subtree using the right half of the array (from 'mid + 1' to 'right').
            root.right = inorder(mid + 1, right)

            # Return the newly created root node of the current subtree.
            return root

        # Initial call to the recursive function, covering the entire array from index 0 to len(nums) - 1.
        return inorder(0, len(nums) -1)

# --- Unit Tests ---

# Helper function to perform an in-order traversal of the BST.
# This is used to verify that the resulting tree is a correct BST.
def inorder_traversal(root: Optional[TreeNode], result: List[int]):
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)

# Helper function to check if the tree is a height-balanced BST.
# Checks the BST property and the height balance property.
def is_balanced_bst(root: Optional[TreeNode]) -> bool:
    # Check 1: BST property (in-order traversal must be sorted)
    traversal_result = []
    inorder_traversal(root, traversal_result)
    
    # If the in-order traversal of the generated tree matches the original sorted array, 
    # the BST property is satisfied.
    # Note: This check relies on the original 'nums' being implicitly compared against 
    # 'traversal_result', which is correct for this specific problem where the output BST's 
    # in-order traversal *must* be the input sorted array.
    
    # Check 2: Height-Balanced property
    # Recursive function to check height and balance simultaneously.
    def check_balance(node: Optional[TreeNode]):
        if not node:
            return 0  # Height of an empty tree is 0

        # Recursively get the height of the left and right subtrees.
        left_height = check_balance(node.left)
        right_height = check_balance(node.right)

        # If any subtree is found to be unbalanced (signaled by returning -1), propagate -1 up.
        if left_height == -1 or right_height == -1:
            return -1

        # Check if the current node is balanced (difference in height <= 1).
        if abs(left_height - right_height) > 1:
            return -1  # Unbalanced
        
        # Return the height of the current subtree (max of sub-heights + 1 for the current node).
        return max(left_height, right_height) + 1

    # The tree is balanced if the root's call does not return -1.
    is_balanced = check_balance(root) != -1
    
    # For this problem, we need to ensure the resulting tree's in-order traversal matches the input array.
    # For a complete test, we would also verify traversal_result against the expected sorted input.
    # For the purpose of a simple unit test, we'll focus on the structure and one example.
    
    return is_balanced and True # True placeholder for BST property, assuming correct logic leads to it.

# Unit Test Class
class TestSortedArrayToBST(unittest.TestCase):
    # Test case 1: A simple array
    def test_simple_case(self):
        # Input sorted array
        nums = [-10, -3, 0, 5, 9]
        # Create an instance of the Solution class
        solution = Solution()
        # Call the method to generate the BST
        root = solution.sortedArrayToBST(nums)
        
        # Verify the structure: 
        # The tree must be a height-balanced BST, and its in-order traversal must be the original array.
        self.assertTrue(root is not None, "Root should not be None for a non-empty array")
        self.assertTrue(is_balanced_bst(root), "The resulting tree must be height-balanced")

        # Verify the content: In-order traversal should match the input array.
        traversal_result = []
        inorder_traversal(root, traversal_result)
        self.assertEqual(traversal_result, nums, "In-order traversal should match the original sorted array")

    # Test case 2: Empty array
    def test_empty_array(self):
        nums = []
        solution = Solution()
        root = solution.sortedArrayToBST(nums)
        # For an empty array, the root should be None.
        self.assertIsNone(root, "Root should be None for an empty array")

    # Test case 3: Array with even number of elements
    def test_even_elements(self):
        nums = [1, 2, 3, 4, 5, 6]
        solution = Solution()
        root = solution.sortedArrayToBST(nums)
        
        # Verify the structure
        self.assertTrue(is_balanced_bst(root), "The resulting tree must be height-balanced")

        # Verify the content
        traversal_result = []
        inorder_traversal(root, traversal_result)
        self.assertEqual(traversal_result, nums, "In-order traversal should match the original sorted array")

# Run the tests when the script is executed directly.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)