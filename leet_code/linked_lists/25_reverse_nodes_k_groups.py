"""
Problem: Reverse Nodes in k-Group - reverse nodes in groups of k

Approach:
- Iterate through the list, checking if k nodes are available
- Reverse each complete k-group using a helper function
- Connect reversed groups using previous tail pointer
- Leave remaining nodes (< k) unreversed
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
    """Solution for LeetCode 25: Reverse Nodes in k-Group."""

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Reverse nodes in groups of k.

        Given a linked list, reverse the nodes k at a time and return its head.
        Nodes less than k at the end should remain in their original order.
        """
        prv_head: Optional[ListNode] = head  # Track k nodes ahead
        k_tail: Optional[ListNode] = None  # Tail of previous reversed group
        new_head: Optional[ListNode] = None  # Head of final result

        while prv_head:
            count: int = 0
            prv_head = head

            # Check if k nodes exist
            while count < k and prv_head:
                prv_head = prv_head.next
                count += 1

            if count == k:
                # Reverse the k-group
                rev_head: Optional[ListNode] = self.reverse_linkedlist(head, k)

                # Set new head on first reversal
                if not new_head:
                    new_head = rev_head

                # Link previous group to current group
                if k_tail:
                    k_tail.next = rev_head

                k_tail = head  # Original head is now tail
                head = prv_head  # Move to next group
            else:
                break

        # Link last reversed group to remainder
        if k_tail:
            k_tail.next = head

        return new_head if new_head else head

    def reverse_linkedlist(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse the first k nodes of a linked list segment."""
        new_head: Optional[ListNode] = None
        while k > 0 and head:
            next_node: Optional[ListNode] = head.next
            head.next = new_head
            new_head = head
            head = next_node
            k -= 1
        return new_head


class TestReverseKGroup(unittest.TestCase):
    """Test cases for Reverse Nodes in k-Group solution."""

    def setUp(self):
        self.solution = Solution()

    def _create_linked_list(self, elements: list) -> Optional[ListNode]:
        """Helper method to create a linked list from a list of values."""
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _get_list_elements(self, head: Optional[ListNode]) -> list:
        """Helper method to convert linked list to array for comparison."""
        elements = []
        current = head
        while current:
            elements.append(current.val)
            current = current.next
        return elements

    def test_example_k2(self):
        """Test with k=2: [1,2,3,4,5]."""
        head = self._create_linked_list([1, 2, 3, 4, 5])
        k = 2
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [2, 1, 4, 3, 5])

    def test_example_k3(self):
        """Test with k=3 and remainder: [1,2,3,4,5]."""
        head = self._create_linked_list([1, 2, 3, 4, 5])
        k = 3
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [3, 2, 1, 4, 5])

    def test_k_equals_list_length(self):
        """Test where k equals list length: [1,2,3]."""
        head = self._create_linked_list([1, 2, 3])
        k = 3
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [3, 2, 1])

    def test_k_greater_than_list_length(self):
        """Test where k is greater than list length: [1,2]."""
        head = self._create_linked_list([1, 2])
        k = 3
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [1, 2])

    def test_empty_list(self):
        """Test with empty list."""
        head = self._create_linked_list([])
        k = 2
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [])

    def test_k_equals_1(self):
        """Test with k=1 (no change): [1,2,3,4]."""
        head = self._create_linked_list([1, 2, 3, 4])
        k = 1
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [1, 2, 3, 4])

    def test_full_reversal_multiple_groups(self):
        """Test full reversal with no remainder: [1,2,3,4,5,6]."""
        head = self._create_linked_list([1, 2, 3, 4, 5, 6])
        k = 2
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [2, 1, 4, 3, 6, 5])

    def test_full_reversal_with_remainder(self):
        """Test with remainder of one node: [1,2,3,4]."""
        head = self._create_linked_list([1, 2, 3, 4])
        k = 3
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [3, 2, 1, 4])

    def test_single_node(self):
        """Test with single node: [1]."""
        head = self._create_linked_list([1])
        k = 2
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [1])

    def test_long_list_k4_remainder3(self):
        """Test with longer list: [1,2,3,4,5,6,7,8,9,10]."""
        head = self._create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        k = 4
        result_head = self.solution.reverseKGroup(head, k)
        self.assertEqual(self._get_list_elements(result_head), [4, 3, 2, 1, 8, 7, 6, 5, 9, 10])


if __name__ == "__main__":
    unittest.main()
