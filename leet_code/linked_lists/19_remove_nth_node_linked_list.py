# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Removes the nth node from the end of a linked list.

        Args:
            head: The head of the linked list.
            n: The position of the node to remove (counting from the end).

        Returns:
            The head of the modified linked list.
        """
        dummy = ListNode(0)  # Create a dummy node to handle edge cases
        dummy.next = head
        slow = dummy
        fast = dummy

        # Move the fast pointer n steps ahead
        for _ in range(n + 1):  # +1 to account for the dummy node
            if (
                fast is None
            ):  # Check if n is larger than the list length, if so, return original list.
                return head
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast:
            slow = slow.next
            fast = fast.next

        # Remove the nth node from the end
        slow.next = slow.next.next

        return dummy.next  # Return the head of the modified list


import unittest


class TestRemoveNthFromEnd(unittest.TestCase):
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

    def test_remove_middle_node(self):
        head = self.create_linked_list([1, 2, 3, 4, 5])
        n = 2
        expected = [1, 2, 3, 5]
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))
        self.assertEqual(result, expected)

    def test_remove_first_node(self):
        head = self.create_linked_list([1, 2, 3])
        n = 3
        expected = [2, 3]
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))
        self.assertEqual(result, expected)

    def test_remove_last_node(self):
        head = self.create_linked_list([1, 2, 3])
        n = 1
        expected = [1, 2]
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))
        self.assertEqual(result, expected)

    def test_remove_single_node(self):
        head = self.create_linked_list([1])
        n = 1
        expected = []
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))
        self.assertEqual(result, expected)

    def test_empty_list(self):
        head = None
        n = 1
        expected = []  # Or None, depending on desired behavior for empty lists
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))

        self.assertEqual(result, expected)

    def test_n_larger_than_list(self):
        head = self.create_linked_list([1, 2])
        n = 5

        expected = [1, 2]
        result = self.linked_list_to_list(Solution().removeNthFromEnd(head, n))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
