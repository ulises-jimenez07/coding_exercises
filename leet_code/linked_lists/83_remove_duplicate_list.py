"""
Problem: Remove duplicates from sorted linked list

Approach:
- Traverse list with single pointer
- Skip nodes with duplicate values
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import (
    List,
    Optional,
)


# --- Linked List Node Definition ---
class ListNode:
    """
    Definition for a singly-linked list node.
    Represents a node containing a value and a pointer to the next node.
    """

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


# --- Solution Class ---
class Solution:
    """
    Contains the method to delete adjacent duplicates from a sorted singly-linked list.
    """

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head

        # Remove duplicates by skipping nodes
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# --- Unit Test Class ---
class TestDeleteDuplicates(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_single_duplicate_pair(self):
        # Test case: A single pair of duplicates (1 -> 1 -> 2 -> 3)
        input_array = [1, 1, 2, 3]
        input_list = self.array_to_list(input_array)
        expected_output = [1, 2, 3]

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_multiple_adjacent_duplicates(self):
        # Test case: Multiple adjacent duplicates (1 -> 1 -> 2 -> 3 -> 3 -> 3)
        input_array = [1, 1, 2, 3, 3, 3]
        input_list = self.array_to_list(input_array)
        expected_output = [1, 2, 3]

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_duplicates_at_head(self):
        # Test case: Duplicates start at the head (4 -> 4 -> 5)
        input_array = [4, 4, 5]
        input_list = self.array_to_list(input_array)
        expected_output = [4, 5]

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_empty_list(self):
        # Test case: An empty list (None)
        input_list = None
        expected_output = []

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(result_list, None)
        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_list_with_all_duplicates(self):
        # Test case: A list where all elements are the same (5 -> 5 -> 5)
        input_array = [5, 5, 5]
        input_list = self.array_to_list(input_array)
        expected_output = [5]

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)

    def test_single_node_list(self):
        # Test case: A list with only one node (9)
        input_array = [9]
        input_list = self.array_to_list(input_array)
        expected_output = [9]

        result_list = self.solution.deleteDuplicates(input_list)

        self.assertEqual(self.list_to_array(result_list), expected_output)


# This block allows the script to be executed and run the unit tests.
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
