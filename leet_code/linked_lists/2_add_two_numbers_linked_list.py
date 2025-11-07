"""
Problem: Add two numbers represented as linked lists

Approach:
- Iterate through both lists simultaneously
- Add digits with carry tracking
- Create new node for each result digit
- Time complexity: O(max(m, n))
- Space complexity: O(max(m, n))
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two non-empty linked lists representing non-negative integers (digits least significant first)
        and returns the sum as a linked list.

        Args:
            l1: The first non-empty linked list.
            l2: The second non-empty linked list.

        Returns:
            The linked list representing the sum of l1 and l2.
        """

        dummy = head = ListNode(0)
        carry = 0

        # Process both lists and carry
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Calculate digit and carry
            carry = total // 10
            head.next = ListNode(total % 10)
            head = head.next

            # Move to next nodes
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


import unittest


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_basic_addition_no_carryover(self):
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6, 4])
        expected = [7, 0, 8]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_addition_with_carryover_all_digits(self):
        l1 = self.create_linked_list([9, 9, 9, 9, 9, 9])
        l2 = self.create_linked_list([9, 9, 9, 9])
        expected = [8, 9, 9, 9, 0, 0, 1]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_lists_with_different_lengths_longer_l1(self):
        l1 = self.create_linked_list([2, 4, 3])
        l2 = self.create_linked_list([5, 6])
        expected = [7, 0, 4]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_lists_with_different_lengths_longer_l2(self):
        l1 = self.create_linked_list([5])
        l2 = self.create_linked_list([5, 6, 4])
        expected = [0, 7, 4]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_empty_lists(self):
        l1 = None
        l2 = None
        expected = []
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_single_digit_lists_with_carry(self):
        l1 = self.create_linked_list([1])
        l2 = self.create_linked_list([9])
        expected = [0, 1]
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.linked_list_to_list(result), expected)


if __name__ == "__main__":
    unittest.main()
