"""
Problem: Swap Nodes in Pairs - swap every two adjacent nodes in a linked list

Approach:
- Use a dummy node to handle edge cases and maintain reference to new head
- Iterate through the list in pairs
- For each pair, reverse the two nodes by adjusting pointers
- Move to the next pair and repeat
- Time complexity: O(n) where n is the number of nodes
- Space complexity: O(1) - only using pointers, no extra space
"""

import unittest
from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """Solution for LeetCode 24: Swap Nodes in Pairs."""

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Swap every two adjacent nodes in a linked list.

        Given a linked list, swap every two adjacent nodes and return its head.
        Must solve without modifying node values, only by changing pointers.
        """
        dummy = ListNode(0)  # Dummy node to simplify edge cases
        dummy.next = head
        prev = dummy  # Track node before the pair to swap

        # Process pairs while both nodes exist
        while head and head.next:
            first = head  # First node of the pair
            second = head.next  # Second node of the pair

            # Perform the swap by adjusting pointers
            prev.next = second  # Previous points to second
            first.next = second.next  # First points to node after second
            second.next = first  # Second points to first

            prev = first  # Move prev to the end of swapped pair
            head = first.next  # Move to next pair

        return dummy.next  # Return new head


class TestSwapPairs(unittest.TestCase):
    """Test cases for Swap Nodes in Pairs solution."""

    def setUp(self):
        self.solution = Solution()

    def _create_list(self, values: list[int]) -> Optional[ListNode]:
        """Helper method to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _list_to_array(self, head: Optional[ListNode]) -> list[int]:
        """Helper method to convert linked list to array for comparison."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_basic_case(self):
        """Test with basic case: [1,2,3,4]."""
        head = self._create_list([1, 2, 3, 4])
        result = self.solution.swapPairs(head)
        expected = [2, 1, 4, 3]
        self.assertEqual(self._list_to_array(result), expected)

    def test_empty_list(self):
        """Test with empty list."""
        head = None
        result = self.solution.swapPairs(head)
        expected = []
        self.assertEqual(self._list_to_array(result), expected)

    def test_single_node(self):
        """Test with single node: [1]."""
        head = self._create_list([1])
        result = self.solution.swapPairs(head)
        expected = [1]
        self.assertEqual(self._list_to_array(result), expected)

    def test_two_nodes(self):
        """Test with two nodes: [1,2]."""
        head = self._create_list([1, 2])
        result = self.solution.swapPairs(head)
        expected = [2, 1]
        self.assertEqual(self._list_to_array(result), expected)

    def test_odd_length(self):
        """Test with odd length: [1,2,3,4,5]."""
        head = self._create_list([1, 2, 3, 4, 5])
        result = self.solution.swapPairs(head)
        expected = [2, 1, 4, 3, 5]
        self.assertEqual(self._list_to_array(result), expected)

    def test_even_length(self):
        """Test with even length: [1,2,3,4,5,6]."""
        head = self._create_list([1, 2, 3, 4, 5, 6])
        result = self.solution.swapPairs(head)
        expected = [2, 1, 4, 3, 6, 5]
        self.assertEqual(self._list_to_array(result), expected)

    def test_three_nodes(self):
        """Test with three nodes: [1,2,3]."""
        head = self._create_list([1, 2, 3])
        result = self.solution.swapPairs(head)
        expected = [2, 1, 3]
        self.assertEqual(self._list_to_array(result), expected)

    def test_long_list(self):
        """Test with longer list: [1,2,3,4,5,6,7,8]."""
        head = self._create_list([1, 2, 3, 4, 5, 6, 7, 8])
        result = self.solution.swapPairs(head)
        expected = [2, 1, 4, 3, 6, 5, 8, 7]
        self.assertEqual(self._list_to_array(result), expected)

    def test_duplicate_values(self):
        """Test with duplicate values: [1,1,2,2]."""
        head = self._create_list([1, 1, 2, 2])
        result = self.solution.swapPairs(head)
        expected = [1, 1, 2, 2]
        self.assertEqual(self._list_to_array(result), expected)

    def test_all_same_values(self):
        """Test with all same values: [5,5,5,5]."""
        head = self._create_list([5, 5, 5, 5])
        result = self.solution.swapPairs(head)
        expected = [5, 5, 5, 5]
        self.assertEqual(self._list_to_array(result), expected)


if __name__ == "__main__":
    unittest.main()
