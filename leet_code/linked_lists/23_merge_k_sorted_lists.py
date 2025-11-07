"""
Problem: Merge k sorted linked lists

Approach:
- Divide and conquer: merge lists pairwise
- Repeatedly merge pairs until one list remains
- Time complexity: O(N log k) where N is total nodes, k is number of lists
- Space complexity: O(1)
"""

from typing import (
    List,
    Optional,
)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def merge_2_lists(self, l1, l2):
        """
        Merges two sorted linked lists into a single sorted linked list.

        Args:
            l1: The head of the first sorted linked list.
            l2: The head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merges k sorted linked lists into a single sorted linked list.

        Args:
            lists: A list of k sorted linked lists.

        Returns:
            The head of the merged sorted linked list, or None if the input list is empty.
        """
        if len(lists) == 0:
            return None

        i = 0
        last = len(lists) - 1
        j = last

        # Merge pairs until one list remains
        while last != 0:
            i = 0
            j = last

            # Merge from both ends
            while j > i:
                lists[i] = self.merge_2_lists(lists[i], lists[j])
                i += 1
                j -= 1
                last = j

        return lists[0]


import unittest


class TestMergeKLists(unittest.TestCase):
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
