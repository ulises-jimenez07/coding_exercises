import unittest
from typing import Optional, List

# --- Linked List Node Definition ---
class ListNode:
    """
    Definition for a singly-linked list node.
    Represents a node containing a value and a pointer to the next node.
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# --- Solution Class ---
class Solution:
    """
    Contains the method to delete adjacent duplicates from a sorted singly-linked list.
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a pointer 'current' to the head of the list.
        current = head
        
        # Traverse the list while 'current' is not None and 'current' has a next node.
        while current and current.next:
            # Check if the value of the current node is equal to the value of the next node.
            if current.val == current.next.val:
                # If they are duplicates, skip the next node (the duplicate) 
                # by setting current.next to current.next.next.
                # 'current' remains at the same position to check for subsequent duplicates.
                current.next = current.next.next
            else:
                # If they are not duplicates, move 'current' to the next node.
                current = current.next
                
        # Return the head of the modified list.
        return head

# --- Unit Test Class ---
class TestDeleteDuplicates(unittest.TestCase):
    """
    Test suite for the Solution.deleteDuplicates method.
    Includes helper methods to manage linked list creation and conversion.
    """

    def array_to_list(self, arr: List[int]) -> Optional[ListNode]:
        """Converts a Python list (array) to a singly-linked list."""
        if not arr:
            return None
        # Create a dummy head to simplify list construction
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def list_to_array(self, head: Optional[ListNode]) -> List[int]:
        """Converts a singly-linked list to a Python list (array)."""
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    def test_no_duplicates(self):
        # Test case: List with no duplicates (1 -> 2 -> 3)
        input_array = [1, 2, 3]
        input_list = self.array_to_list(input_array)
        expected_output = input_array
        
        solution = Solution() 
        result_list = solution.deleteDuplicates(input_list) 
        
        # Assert that the resulting array representation matches the expected output
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_single_duplicate_pair(self):
        # Test case: A single pair of duplicates (1 -> 1 -> 2 -> 3)
        input_array = [1, 1, 2, 3]
        input_list = self.array_to_list(input_array)
        expected_output = [1, 2, 3]
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_multiple_adjacent_duplicates(self):
        # Test case: Multiple adjacent duplicates (1 -> 1 -> 2 -> 3 -> 3 -> 3)
        input_array = [1, 1, 2, 3, 3, 3]
        input_list = self.array_to_list(input_array)
        expected_output = [1, 2, 3]
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_duplicates_at_head(self):
        # Test case: Duplicates start at the head (4 -> 4 -> 5)
        input_array = [4, 4, 5]
        input_list = self.array_to_list(input_array)
        expected_output = [4, 5]
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_empty_list(self):
        # Test case: An empty list (None)
        input_list = None
        expected_output = []
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(result_list, None)
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_list_with_all_duplicates(self):
        # Test case: A list where all elements are the same (5 -> 5 -> 5)
        input_array = [5, 5, 5]
        input_list = self.array_to_list(input_array)
        expected_output = [5]
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_single_node_list(self):
        # Test case: A list with only one node (9)
        input_array = [9]
        input_list = self.array_to_list(input_array)
        expected_output = [9]
        
        solution = Solution()
        result_list = solution.deleteDuplicates(input_list)
        
        self.assertEqual(self.list_to_array(result_list), expected_output)

# This block allows the script to be executed and run the unit tests.
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)