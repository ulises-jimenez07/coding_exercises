"""
Problem: Reverse a singly linked list

Approaches:
1. Iterative:
   - Use three pointers: prev, current, and next
   - Iterate through list, reversing links one by one
   - Time complexity: O(n), Space complexity: O(1)
2. Recursive:
   - Reverse the sub-list starting from the second node
   - Hook the first node back to the end of the reversed sub-list
   - Time complexity: O(n), Space complexity: O(n) due to recursion stack
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """Node definition for a singly linked list."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """Contains methods to reverse a singly linked list."""

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.
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

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list recursively.
        """
        # Base case: if list is empty or has only one node, it's already reversed
        if not head or not head.next:
            return head

        # We drill down to the end of the list first.
        # 'new_head' will eventually be the very last node of the original list.
        new_head = self.reverseListRecursive(head.next)

        # Magical part:
        # After returning from recursion, head.next is the node we just processed.
        # We want that node to point back to 'head' to reverse the link.
        # Example: 1 -> 2 -> 3. If head is 2, head.next is 3.
        # head.next.next = head makes 3 point back to 2.
        head.next.next = head

        # Set current head's next to None to break the old forward link
        # and avoid creating a cycle (2 -> 3 -> 2).
        head.next = None

        # Return the same new_head (the original tail) all the way up the stack.
        return new_head


class TestReverseList(unittest.TestCase):
    """Unit tests for linked list reversal implementations."""

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

    def test_recursive_reversal(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseListRecursive(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])

    def test_recursive_empty(self):
        head = self.create_linked_list([])
        reversed_head = self.solution.reverseListRecursive(head)
        self.assertIsNone(reversed_head)


if __name__ == "__main__":
    unittest.main()
