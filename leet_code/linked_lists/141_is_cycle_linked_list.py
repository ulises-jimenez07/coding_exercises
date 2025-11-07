"""
Problem: Detect if a linked list has a cycle

Approach:
- Use Floyd's cycle detection (two pointers: fast and slow)
- Fast pointer moves 2 steps, slow moves 1 step
- If they meet, there's a cycle
- Time complexity: O(n)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle using the fast and slow pointer approach.

        Args:
            head: The head of the linked list.

        Returns:
            True if the linked list has a cycle, False otherwise.
        """
        fast = head
        slow = head

        # Fast moves 2 steps, slow moves 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # If pointers meet, cycle exists
            if slow == fast:
                return True

        return False


class TestHasCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values, pos):
        """
        Creates a linked list with an optional cycle.

        Args:
            values: A list of values to create the linked list from.
            pos: The index of the node to create the cycle. If -1, no cycle is created.

        Returns:
            The head of the linked list.
        """
        nodes = []
        for val in values:
            nodes.append(ListNode(val))
        for i in range(len(values) - 1):
            nodes[i].next = nodes[i + 1]
        if pos != -1:
            nodes[-1].next = nodes[pos]  # Create the cycle
        return nodes[0] if nodes else None

    def test_has_cycle(self):
        head = self.create_linked_list([3, 2, 0, -4], 1)
        self.assertTrue(self.solution.hasCycle(head))

    def test_no_cycle(self):
        head = self.create_linked_list([1, 2], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_single_node_no_cycle(self):
        head = self.create_linked_list([1], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_empty_list(self):
        head = self.create_linked_list([], -1)
        self.assertFalse(self.solution.hasCycle(head))

    def test_cycle_at_end(self):  # New test case: Cycle at the end
        head = self.create_linked_list([1, 2, 3, 4], 3)
        self.assertTrue(self.solution.hasCycle(head))

    def test_cycle_at_beginning(self):
        head = self.create_linked_list([1, 2, 3], 0)
        self.assertTrue(self.solution.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
