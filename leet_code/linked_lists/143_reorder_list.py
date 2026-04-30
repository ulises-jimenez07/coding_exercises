"""
Problem: Reorder a linked list in the pattern L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...

Approach:
- Find middle of list using slow/fast pointers
- Reverse the second half
- Merge both halves by alternating nodes
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest


# Definition for singly-linked list.
class ListNode:
    """Node in a singly linked list."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """Solution for reordering a linked list in-place."""

    def reorderList(self, head):
        """
        Reorders list in-place to alternate between start and end nodes.
        """

        def find_mid(head):
            # Use slow/fast pointers to find middle
            slow = fast = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            # Reverse linked list
            prev = None
            curr = head
            while curr:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_
            return prev

        mid = find_mid(head)
        second = reverse(mid)
        first = head

        # Merge by alternating nodes from first and second halves
        while second.next:
            next_ = first.next
            first.next = second
            first = next_

            next_ = second.next
            second.next = first
            second = next_

        return head


class TestReorderList(unittest.TestCase):
    """Unit tests for Solution.reorderList."""

    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper function to create a linked list from a list of values."""
        head = None
        tail = None
        for val in values:
            node = ListNode(val)
            if head is None:
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

    def test_reorder_list_odd_length(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        expected = [1, 5, 2, 4, 3]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_reorder_list_even_length(self):
        head = self.create_linked_list([1, 2, 3, 4])
        expected = [1, 4, 2, 3]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_reorder_single_node(self):
        head = self.create_linked_list([1])
        expected = [1]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_reorder_two_nodes(self):
        head = self.create_linked_list([1, 2])
        expected = [1, 2]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_reorder_three_nodes(self):
        head = self.create_linked_list([1, 2, 3])
        expected = [1, 3, 2]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)

    def test_reorder_longer_list(self):
        head = self.create_linked_list([1, 2, 3, 4, 5, 6, 7, 8])
        expected = [1, 8, 2, 7, 3, 6, 4, 5]
        self.solution.reorderList(head)
        result = self.linked_list_to_list(head)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
