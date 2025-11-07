"""
Problem: Find the node where the cycle begins in a linked list

Approach:
- Use Floyd's cycle detection to find if cycle exists
- Once detected, reset one pointer to head
- Move both pointers one step until they meet at cycle start
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


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
        fast = head
        slow = head
        inter_point = None

        # Detect cycle using fast and slow pointers
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break

        # No cycle found
        if fast is None or fast.next is None:
            return None

        # Find cycle start by moving both pointers one step
        inter_point = slow
        start = head
        while start != inter_point:
            start = start.next
            inter_point = inter_point.next

        return start


class TestDetectCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

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
        head = self.create_linked_list([1, 2, 3, 4, 5])
        self.assertIsNone(self.solution.detectCycle(head))

    def test_cycle_at_beginning(self):
        head = self.create_linked_list([1, 2, 3, 4, 5], 0)
        self.assertEqual(self.solution.detectCycle(head).val, 1)

    def test_cycle_in_middle(self):
        head = self.create_linked_list([1, 2, 3, 4, 5], 2)
        self.assertEqual(self.solution.detectCycle(head).val, 3)

    def test_single_node_no_cycle(self):
        head = ListNode(1)
        self.assertIsNone(self.solution.detectCycle(head))

    def test_single_node_with_cycle(self):
        head = ListNode(1)
        head.next = head
        self.assertEqual(self.solution.detectCycle(head).val, 1)

    def test_empty_list(self):
        self.assertIsNone(self.solution.detectCycle(None))


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
