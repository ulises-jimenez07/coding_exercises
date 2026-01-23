"""
Problem: Merge k sorted linked lists

Approach:
- Version 1: Divide and conquer: merge lists pairwise (O(N log k) time, O(1) space)
- Version 2: Min-Heap (Priority Queue): merge using a heap of current heads (O(N log k) time, O(k) space)
"""

import heapq
import unittest
from typing import (
    Any,
    List,
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val: int = 0, next_node: Optional["ListNode"] = None):
        self.val = val
        self.next = next_node

    def __lt__(self, other: Any) -> bool:
        """Less-than operator for heap comparison."""
        if not isinstance(other, ListNode):
            return NotImplemented
        return self.val < other.val


class Solution:
    """Solution class for merging k sorted lists."""

    def merge_2_lists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a single sorted linked list.
        """
        curr = ListNode(0)
        ans = curr
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next
            else:
                curr.next = l1
                l1 = l1.next

            curr = curr.next
        curr.next = l2 if l1 is None else l1
        return ans.next

    def merge_k_lists_divide_and_conquer(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Version 1: Divide and Conquer
        Time Complexity: O(N log k) - where N is the total number of nodes and k is the number of lists.
        Space Complexity: O(1) - if we ignore the recursive stack or if implemented iteratively.
        """
        if not lists:
            return None

        last = len(lists) - 1

        # Merge pairs until only one list is left at index 0
        while last != 0:
            i = 0
            j = last

            # Merge lists from both ends of the current range
            while j > i:
                lists[i] = self.merge_2_lists(lists[i], lists[j])
                i += 1
                j -= 1

            # Update the last index to the end of the merged lists
            last = j

        return lists[0]

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Version 2: Min-Heap (Priority Queue)
        Time Complexity: O(N log k) - each insertion/deletion in the heap takes O(log k).
        Space Complexity: O(k) - the heap stores at most k nodes at any time.
        """
        heap: List[ListNode] = []
        # Push the head of each linked list into the heap
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        # Dummy node to simplify the construction of the result list
        dummy = ListNode(-1)
        curr = dummy

        # Continuously pop the smallest element from the heap and add it to the result
        while heap:
            smallest_node = heapq.heappop(heap)
            curr.next = smallest_node
            curr = curr.next

            # If the popped node has a next element, push it into the heap
            if smallest_node.next:
                heapq.heappush(heap, smallest_node.next)

        return dummy.next


class TestMergeKLists(unittest.TestCase):
    """Unit tests for mergeKLists solutions."""

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

    def test_empty_list(self):
        lists = []
        merged_list = self.solution.mergeKLists(lists)
        self.assertIsNone(merged_list)

    def test_single_list(self):
        lists = [self.create_linked_list([1, 4, 5])]
        merged_list = self.solution.mergeKLists(lists)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 4, 5])

    def test_multiple_lists(self):
        lists = [
            self.create_linked_list([1, 4, 5]),
            self.create_linked_list([1, 3, 4]),
            self.create_linked_list([2, 6]),
        ]
        merged_list = self.solution.mergeKLists(lists)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 1, 2, 3, 4, 4, 5, 6])

    def test_with_empty_lists(self):
        lists = [
            self.create_linked_list([1, 4, 5]),
            None,
            self.create_linked_list([2, 6]),
        ]
        merged_list = self.solution.mergeKLists(lists)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 2, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
