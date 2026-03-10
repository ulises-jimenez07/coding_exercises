"""
Problem: Flatten a Multilevel Doubly Linked List.
Flatten the list such that all nodes appear in a single-level doubly linked list.

Approach:
- Iterate through the list.
- When a node with a child is found:
    1. Find the tail of the child list.
    2. Insert the child list between the current node and its next node.
    3. Update all necessary prev/next pointers.
    4. Set child pointer to None.
- Time complexity: O(n) where n is the total number of nodes.
- Space complexity: O(1) in terms of extra space used (excluding node allocations).
"""

import unittest
from typing import Optional


class Node:
    """Definition for a Node in a multilevel doubly linked list."""

    def __init__(
        self,
        val: int,
        prev: Optional["Node"] = None,
        next_node: Optional["Node"] = None,
        child: Optional["Node"] = None,
    ):
        """Initializes a node with value, prev, next, and child pointers."""
        self.val: int = val
        self.prev: Optional[Node] = prev
        self.next: Optional[Node] = next_node
        self.child: Optional[Node] = child


class Solution:
    """Solution for flattening a multilevel doubly linked list."""

    def flatten(self, head: Optional[Node]) -> Optional[Node]:
        """Flattens the multilevel linked list into a single level."""
        if not head:
            return None

        curr = head
        while curr:
            # If current node has no child, proceed to the next node
            if not curr.child:
                curr = curr.next
                continue

            # Remember the next node in the current level
            next_node = curr.next

            # Find the child list head and iterate to find its tail
            child_head = curr.child
            child_tail = child_head
            while child_tail.next:
                child_tail = child_tail.next

            # Point current node's next to child head and update prev
            curr.next = child_head
            child_head.prev = curr

            # Connect child tail to the original next node
            if next_node:
                child_tail.next = next_node
                next_node.prev = child_tail

            # Clear the child pointer as it's now flattened
            curr.child = None
            curr = curr.next

        return head


class TestFlattenLinkedList(unittest.TestCase):
    """Unit tests for the multilevel flattening logic."""

    def test_example_1(self) -> None:
        """Tests LeetCode Example 1: 3-level list."""
        # Level 1: 1 <-> 2 <-> 3 <-> 4 <-> 5 <-> 6
        n1 = Node(1)
        n2 = Node(2, n1)
        n1.next = n2
        n3 = Node(3, n2)
        n2.next = n3
        n4 = Node(4, n3)
        n3.next = n4
        n5 = Node(5, n4)
        n4.next = n5
        n6 = Node(6, n5)
        n5.next = n6

        # Level 2 (child of 3): 7 <-> 8 <-> 9 <-> 10
        n7 = Node(7)
        n8 = Node(8, n7)
        n7.next = n8
        n9 = Node(9, n8)
        n8.next = n9
        n10 = Node(10, n9)
        n9.next = n10
        n3.child = n7

        # Level 3 (child of 8): 11 <-> 12
        n11 = Node(11)
        n12 = Node(12, n11)
        n11.next = n12
        n8.child = n11

        solution = Solution()
        head = solution.flatten(n1)

        # Expected sequence: 1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6
        expected = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            # Verify child is None
            self.assertIsNone(curr.child, f"Node {curr.val} still has a child.")
            # Verify double linkage
            if curr.next:
                self.assertEqual(curr.next.prev, curr, f"Linkage error at node {curr.val}")
            curr = curr.next

        for i, val in enumerate(expected):
            self.assertEqual(result[i], val, f"Mismatch at index {i}")

    def test_empty_list(self) -> None:
        """Tests behavior with an empty list."""
        solution = Solution()
        self.assertIsNone(solution.flatten(None))

    def test_single_node(self) -> None:
        """Tests behavior with a single node (no child)."""
        n1 = Node(10)
        solution = Solution()
        head = solution.flatten(n1)
        self.assertEqual(head.val, 10)
        self.assertIsNone(head.next)
        self.assertIsNone(head.prev)
        self.assertIsNone(head.child)

    def test_simple_child(self) -> None:
        """Tests a simple head node with a single child point."""
        n1 = Node(1)
        n2 = Node(2)
        n1.child = n2

        solution = Solution()
        head = solution.flatten(n1)
        self.assertEqual(head.val, 1)
        self.assertEqual(head.next.val, 2)
        self.assertEqual(head.next.prev, head)
        self.assertIsNone(head.child)


if __name__ == "__main__":
    unittest.main()
