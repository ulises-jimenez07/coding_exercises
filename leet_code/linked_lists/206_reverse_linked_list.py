"""
Problem: Reverse a singly linked list

Approach:
- Use three pointers: prev, current, and next
- Iterate through list, reversing links one by one
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the reversed linked list.
        """
        prev = None
        while head:
            next_node = head.next
            # Reverse the link
            head.next = prev

            # Move pointers forward
            prev = head
            head = next_node
        return prev


class TestReverseList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper function to create a linked list from a list of values."""
        head = None
        tail = None
        for val in values:
            node = ListNode(val)
            if not head:
                head = node
                tail = node
            else:
                tail.next = node
                tail = node
        return head

    def linked_list_to_list(self, head):
        """Helper function to convert a linked list to a list of values."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_empty_list(self):
        head = self.create_linked_list([])
        reversed_head = self.solution.reverseList(head)
        self.assertIsNone(reversed_head)

    def test_single_element_list(self):
        head = self.create_linked_list([5])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5])

    def test_multiple_elements_list(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
