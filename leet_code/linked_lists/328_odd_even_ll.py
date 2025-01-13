# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def oddEvenList(self, head):
        """
        Groups all odd nodes together followed by the even nodes in a linked list.
        The relative order inside both the even and odd groups should remain as it was in the input.
        The first node is considered odd, the second node even and so on ...

        Args:
            head: The head of the linked list.

        Returns:
            The head of the modified linked list.
        """
        if not head:
            return head

        odd = head
        even = head.next
        even_head = even  # Store the head of the even list

        while even and even.next:
            odd.next = even.next  # Connect odd node to the next odd node
            odd = odd.next
            even.next = odd.next  # Connect even node to the next even node
            even = even.next

        odd.next = even_head  # Connect the end of the odd list to the beginning of the even list
        return head


import unittest


class TestOddEvenList(unittest.TestCase):
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
        reordered_head = Solution().oddEvenList(head)
        self.assertIsNone(reordered_head)

    def test_single_node(self):
        head = self.create_linked_list([1])
        reordered_head = Solution().oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(reordered_head), [1])

    def test_two_nodes(self):
        head = self.create_linked_list([1, 2])
        reordered_head = Solution().oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(reordered_head), [1, 2])

    def test_multiple_nodes(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        reordered_head = Solution().oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(reordered_head), [1, 3, 5, 2, 4])

    def test_even_number_of_nodes(self):
        head = self.create_linked_list([1, 2, 3, 4, 5, 6])
        reordered_head = Solution().oddEvenList(head)
        self.assertEqual(self.linked_list_to_list(reordered_head), [1, 3, 5, 2, 4, 6])


if __name__ == "__main__":
    unittest.main()
