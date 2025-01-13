# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Merges two sorted linked lists into a new sorted linked list.

        Args:
            list1: The first sorted linked list.
            list2: The second sorted linked list.

        Returns:
            A new sorted linked list containing all elements from list1 and list2,
            or None if both input lists are None.
        """
        # Create a dummy node to simplify the merging process.
        dummy = ListNode(0)  # Use a more descriptive name
        # Store the head of the merged list.  Using a separate variable is slightly clearer
        tail = dummy

        # Iterate while both lists have elements.
        while list1 and list2:
            # Compare the current elements and add the smaller one to the merged list.
            if list1.val <= list2.val:  # Use <= to maintain stability
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # Move to the next node in the merged list.
            tail = tail.next

        # Add the remaining elements from list1 or list2 (only one will be non-empty at this point)
        tail.next = list1 or list2  # More concisely handles remaining elements.

        # Return the head of the merged list (excluding the dummy node).
        return dummy.next


# Test cases using unittest
class TestMergeTwoLists(unittest.TestCase):
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

    def test_both_lists_non_empty(self):
        list1 = self.create_linked_list([1, 2, 4])
        list2 = self.create_linked_list([1, 3, 4])
        merged_list = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 1, 2, 3, 4, 4])

    def test_one_list_empty(self):
        list1 = self.create_linked_list([1, 2, 4])
        list2 = None
        merged_list = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 2, 4])

    def test_both_lists_empty(self):
        list1 = None
        list2 = None
        merged_list = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged_list), [])

    def test_one_list_longer(self):
        list1 = self.create_linked_list([1, 2])
        list2 = self.create_linked_list([1, 3, 4, 5])
        merged_list = Solution().mergeTwoLists(list1, list2)
        self.assertEqual(self.linked_list_to_list(merged_list), [1, 1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
