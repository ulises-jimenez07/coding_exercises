"""
Problem: Check if a linked list is a palindrome

Approach:
- Find middle using fast/slow pointers
- Reverse second half of list
- Compare first and second halves
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


class ListNode:
    """Node definition for a singly linked list."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """Provides a solution for checking if a linked list is a palindrome."""

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a singly linked list is a palindrome.
        """

        def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Find middle and reverse second half
        middle = find_middle(head)
        second_half_reversed = reverse(middle)

        first_half = head
        second_half = second_half_reversed

        # Compare both halves
        while first_half and second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

        return True


class TestIsPalindrome(unittest.TestCase):
    """Unit tests for verifying the isPalindrome implementation."""

    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values: list[int]) -> Optional[ListNode]:
        """Helper function to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        return head

    def test_empty_list(self):
        self.assertTrue(self.solution.isPalindrome(None))

    def test_single_node_list(self):
        head = self.create_linked_list([1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_palindrome_odd_length(self):
        head = self.create_linked_list([1, 2, 3, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_palindrome_even_length(self):
        head = self.create_linked_list([1, 2, 2, 1])
        self.assertTrue(self.solution.isPalindrome(head))

    def test_not_palindrome_odd_length(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertFalse(self.solution.isPalindrome(head))

    def test_not_palindrome_even_length(self):
        head = self.create_linked_list([1, 2, 3, 1])
        self.assertFalse(self.solution.isPalindrome(head))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
