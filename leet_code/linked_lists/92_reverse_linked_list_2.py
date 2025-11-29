"""
Problem: Reverse Linked List II - Reverse a linked list from position left to right.

Approach:
- Use a dummy node to simplify edge cases (e.g., reversing from head).
- Traverse to the node just before the 'left' position.
- Reverse the sublist from 'left' to 'right'.
- Reconnect the reversed sublist with the rest of the list.
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """
    Definition for a singly-linked list node.
    """

    def __init__(self, val=0, next=None):  # pylint: disable=redefined-builtin
        self.val = val
        self.next = next


class Solution:
    """
    Solution class for Reverse Linked List II problem.
    """

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverses the nodes of the list from position left to right.
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        connector = dummy

        # Move connector to the node just before the 'left' position
        for _ in range(left - 1):
            connector = connector.next

        # curr is the first node to be reversed
        curr = connector.next
        # tail will be the last node of the reversed sublist (which is curr initially)
        tail = curr
        prev = None

        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Connect the end of the reversed sublist to the rest of the list
        tail.next = curr

        # Connect the node before the reversed sublist to the start of the reversed sublist
        connector.next = prev

        return dummy.next


class TestReverseLinkedListII(unittest.TestCase):
    """
    Unit tests for Reverse Linked List II solution.
    """

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

    def test_reverse_middle(self):
        """Test reversing a sublist in the middle: [1,2,3,4,5], left=2, right=4 -> [1,4,3,2,5]"""
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = self.solution.reverseBetween(head, 2, 4)
        self.assertEqual(self.linked_list_to_list(reversed_head), [1, 4, 3, 2, 5])

    def test_reverse_head(self):
        """Test reversing from the head: [5], left=1, right=1 -> [5]"""
        head = self.create_linked_list([5])
        reversed_head = self.solution.reverseBetween(head, 1, 1)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5])

    def test_reverse_full_list(self):
        """Test reversing the entire list: [1, 2], left=1, right=2 -> [2, 1]"""
        head = self.create_linked_list([1, 2])
        reversed_head = self.solution.reverseBetween(head, 1, 2)
        self.assertEqual(self.linked_list_to_list(reversed_head), [2, 1])

    def test_reverse_tail(self):
        """Test reversing at the tail: [1, 2, 3], left=2, right=3 -> [1, 3, 2]"""
        head = self.create_linked_list([1, 2, 3])
        reversed_head = self.solution.reverseBetween(head, 2, 3)
        self.assertEqual(self.linked_list_to_list(reversed_head), [1, 3, 2])


if __name__ == "__main__":
    unittest.main()
