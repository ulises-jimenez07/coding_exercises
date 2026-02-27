"""
Problem: Sort a linked list in O(n log n) time and O(1) space (excluding recursion stack).

Approach:
- Merge sort on linked list: split at middle, recursively sort halves, merge
- Split using slow/fast pointers to find midpoint
- Merge two sorted lists with dummy node
- Time complexity: O(n log n)
- Space complexity: O(log n) recursion stack

Example: 4->2->1->3 -> 1->2->3->4
"""

import unittest
from typing import Optional


class ListNode:
    """Singly-linked list node."""

    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node


class Solution:
    """
    Merge sort on linked list: split, sort recursively, merge.
    """

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        second_head = self.split_list(head)
        first_half_sorted = self.sortList(head)
        second_half_sorted = self.sortList(second_head)

        return self.merge(first_half_sorted, second_half_sorted)

    def split_list(self, head: ListNode) -> ListNode:
        """Split list at middle using slow/fast pointers. Returns head of second half."""
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second_head = slow.next
        slow.next = None
        return second_head

    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted lists. Returns head of merged list."""
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        return dummy.next


class TestSortList(unittest.TestCase):
    """Unit tests for Sort List implementation."""

    def setUp(self):
        self.solution = Solution()

    def _create_list(self, values: list[int]) -> Optional[ListNode]:
        """Build linked list from values."""
        if not values:
            return None
        head = ListNode(values[0])
        tail = head
        for val in values[1:]:
            tail.next = ListNode(val)
            tail = tail.next
        return head

    def _to_list(self, head: Optional[ListNode]) -> list[int]:
        """Convert linked list to Python list."""
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_example(self):
        """Tests LeetCode example: [4,2,1,3] -> [1,2,3,4]."""
        head = self._create_list([4, 2, 1, 3])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [1, 2, 3, 4])

    def test_single_node(self):
        """Tests single node returns unchanged."""
        head = self._create_list([1])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [1])

    def test_two_nodes(self):
        """Tests two nodes: [2,1] -> [1,2]."""
        head = self._create_list([2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [1, 2])

    def test_already_sorted(self):
        """Tests already sorted list."""
        head = self._create_list([1, 2, 3])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [1, 2, 3])

    def test_reverse_sorted(self):
        """Tests reverse sorted: [3,2,1] -> [1,2,3]."""
        head = self._create_list([3, 2, 1])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [1, 2, 3])

    def test_with_negatives(self):
        """Tests list with negative values."""
        head = self._create_list([-1, 5, 3, 4, 0])
        result = self.solution.sortList(head)
        self.assertEqual(self._to_list(result), [-1, 0, 3, 4, 5])

    def test_empty_list(self):
        """Tests None input returns None."""
        result = self.solution.sortList(None)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
