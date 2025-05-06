# Definition for singly-linked list.
from typing import Optional
import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Detects if a cycle exists in a singly linked list and returns the node where the cycle begins.

        Args:
            head: The head of the linked list.

        Returns:
            The node where the cycle begins, or None if there is no cycle.
        """
        # Initialize two pointers, fast and slow, both starting at the head of the list.
        fast = head
        slow = head
        # Initialize a variable to store the intersection point of the fast and slow pointers.
        inter_point = None

        # Traverse the list with the fast pointer moving two steps at a time and the slow pointer moving one step at a time.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # If the fast and slow pointers meet, it indicates the presence of a cycle.
            if slow == fast:
                break

        # If the fast pointer reaches the end of the list (or the next node is None), there is no cycle.
        if fast is None or fast.next is None:
            return None

        # If a cycle is detected, the slow pointer is at the intersection point.
        inter_point = slow
        # Reset the slow pointer (now named 'start') to the head of the list.
        start = head
        # Move both the 'start' pointer and the 'inter_point' pointer one step at a time.
        # The point where they meet is the starting node of the cycle.
        while start != inter_point:
            start = start.next
            inter_point = inter_point.next

        # Return the starting node of the cycle.
        return start


class TestDetectCycle(unittest.TestCase):
    def create_linked_list(self, values, pos=-1):
        """Helper function to create a linked list, with an optional cycle."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        nodes = [head]
        for i in range(1, len(values)):
            node = ListNode(values[i])
            current.next = node
            current = node
            nodes.append(node)
        if pos != -1:
            current.next = nodes[pos]
        return head

    def test_no_cycle(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertIsNone(solution.detectCycle(head))

    def test_cycle_at_beginning(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5], 0)
        self.assertEqual(solution.detectCycle(head).val, 1)

    def test_cycle_in_middle(self):
        solution = Solution()
        head = self.create_linked_list([1, 2, 3, 4, 5], 2)
        self.assertEqual(solution.detectCycle(head).val, 3)

    def test_single_node_no_cycle(self):
        solution = Solution()
        head = ListNode(1)
        self.assertIsNone(solution.detectCycle(head))

    def test_single_node_with_cycle(self):
        solution = Solution()
        head = ListNode(1)
        head.next = head
        self.assertEqual(solution.detectCycle(head).val, 1)

    def test_empty_list(self):
        solution = Solution()
        self.assertIsNone(solution.detectCycle(None))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
