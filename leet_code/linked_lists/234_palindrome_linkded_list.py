# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a singly linked list is a palindrome.

        Args:
            head (Optional[ListNode]): The head of the singly linked list.

        Returns:
            bool: True if the linked list is a palindrome, False otherwise.
        """

        def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
            """
            Finds the middle node of a singly linked list using the two-pointer (slow and fast) approach.
            If the list has an even number of nodes, it returns the second middle node.

            Args:
                head (Optional[ListNode]): The head of the singly linked list.

            Returns:
                Optional[ListNode]: The middle node of the linked list.
            """
            slow = head
            fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            """
            Reverses a singly linked list iteratively.

            Args:
                head (Optional[ListNode]): The head of the singly linked list to be reversed.

            Returns:
                Optional[ListNode]: The head of the reversed linked list.
            """
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Find the middle of the linked list
        middle = find_middle(head)

        # Reverse the second half of the linked list
        second_half_reversed = reverse(middle)

        # Compare the first half and the reversed second half
        first_half = head
        second_half = second_half_reversed

        while second_half:
            if first_half.val != second_half.val:
                return False  # Values don't match, not a palindrome
            first_half = first_half.next
            second_half = second_half.next

        return True  # All values matched, it's a palindrome


class TestIsPalindrome(unittest.TestCase):
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
        solution = Solution()
        self.assertTrue(solution.isPalindrome(None))

    def test_single_node_list(self):
        solution = Solution()
        head = self.create_linked_list([1])
        self.assertTrue(solution.isPalindrome(head))

    def test_palindrome_odd_length(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 2, 1])
        self.assertTrue(solution.isPalindrome(head))

    def test_palindrome_even_length(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 2, 1])
        self.assertTrue(solution.isPalindrome(head))

    def test_not_palindrome_odd_length(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertFalse(solution.isPalindrome(head))

    def test_not_palindrome_even_length(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 1])
        self.assertFalse(solution.isPalindrome(head))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
