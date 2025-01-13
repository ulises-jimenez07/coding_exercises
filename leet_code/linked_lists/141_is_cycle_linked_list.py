from typing import Optional
import unittest


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
        fast = head  # Fast pointer moves two steps at a time
        slow = head  # Slow pointer moves one step at a time

        while fast and fast.next:  # Check if fast pointer and its next node exist
            fast = fast.next.next  # Move fast pointer two steps
            slow = slow.next  # Move slow pointer one step
            if slow == fast:  # Cycle detected if slow and fast pointers meet
                return True

        return False  # No cycle found


class TestHasCycle(unittest.TestCase):
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
        self.assertTrue(Solution().hasCycle(head))

    def test_no_cycle(self):
        head = self.create_linked_list([1, 2], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_single_node_no_cycle(self):
        head = self.create_linked_list([1], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_empty_list(self):
        head = self.create_linked_list([], -1)
        self.assertFalse(Solution().hasCycle(head))

    def test_cycle_at_end(self):  # New test case: Cycle at the end
        head = self.create_linked_list([1, 2, 3, 4], 3)  # Cycle back to last node
        self.assertTrue(Solution().hasCycle(head))

    def test_cycle_at_beginning(self):
        head = self.create_linked_list([1, 2, 3], 0)  # Cycle back to the first node
        self.assertTrue(Solution().hasCycle(head))


if __name__ == "__main__":
    unittest.main()
