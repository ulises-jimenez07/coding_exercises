from typing import Optional
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.

        Args:
            head: The head of the linked list.

        Returns:
            The head of the reversed linked list.
        """
        prev = None
        while head:
            next_node = head.next  # Store the next node
            head.next = prev  # Reverse the pointer

            prev = head  # Move prev forward
            head = next_node  # Move head forward
        return prev


class TestReverseList(unittest.TestCase):
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
        reversed_head = Solution().reverseList(head)
        self.assertIsNone(reversed_head)

    def test_single_element_list(self):
        head = self.create_linked_list([5])
        reversed_head = Solution().reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5])

    def test_multiple_elements_list(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reversed_head = Solution().reverseList(head)
        self.assertEqual(self.linked_list_to_list(reversed_head), [5, 4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
