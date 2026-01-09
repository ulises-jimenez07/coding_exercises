"""
Problem: Flatten a multi-level linked list.

Approach:
- Maintain a tail pointer to track the end of the first level.
- Traverse the list and append any child chains to the tail.
- Update the tail pointer as new children are added.
- Time Complexity: O(n) where n is the total number of nodes.
- Space Complexity: O(1) as modification is in-place.
"""

import unittest
from typing import Optional


class MultiLevelListNode:
    """Node definition for a multi-level linked list."""

    def __init__(self, val=None, next_node=None, child=None):
        """Initializes a node with optional next and child pointers."""
        self.val = val
        self.next = next_node
        self.child = child


class Solution:
    """Provides a solution for flattening a multi-level linked list."""

    def flatten(self, head: Optional[MultiLevelListNode]) -> Optional[MultiLevelListNode]:
        """
        Flattens the multi-level list by appending children to the end of the main level.
        """
        if not head:
            return None

        # Find the initial tail of the first level
        tail = head
        while tail.next:
            tail = tail.next

        curr = head
        while curr:
            # If child exists, append it to the tail
            if curr.child:
                tail.next = curr.child
                curr.child = None

                # Traverse to the new tail of the list
                while tail.next:
                    tail = tail.next

            curr = curr.next

        return head


class TestFlattenMultiLevelList(unittest.TestCase):
    """Unit tests for verifying the multi-level list flattening logic."""

    def setUp(self):
        """Sets up the test case with a Solution instance."""
        self.solution = Solution()

    def get_list_values(self, head: Optional[MultiLevelListNode]) -> list:
        """Helper to convert linked list to a list of values."""
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        return values

    def test_empty_list(self):
        """Tests behavior with a None head."""
        self.assertIsNone(self.solution.flatten(None))

    def test_single_element(self):
        """Tests behavior with a single node."""
        head = MultiLevelListNode(1)
        flattened = self.solution.flatten(head)
        self.assertEqual(self.get_list_values(flattened), [1])

    def test_flat_list(self):
        """Tests behavior with a list that has no children."""
        n1 = MultiLevelListNode(1)
        n2 = MultiLevelListNode(2)
        n1.next = n2
        flattened = self.solution.flatten(n1)
        self.assertEqual(self.get_list_values(flattened), [1, 2])

    def test_simple_child(self):
        """Tests a simple list with one nested child."""
        # 1 -> 2
        #      |
        #      3 -> 4
        n1 = MultiLevelListNode(1)
        n2 = MultiLevelListNode(2)
        n3 = MultiLevelListNode(3)
        n4 = MultiLevelListNode(4)

        n1.next = n2
        n2.child = n3
        n3.next = n4

        flattened = self.solution.flatten(n1)
        result = self.get_list_values(flattened)
        expected = [1, 2, 3, 4]

        # Use enumerate to verify result values
        for i, val in enumerate(result):
            self.assertEqual(val, expected[i])

    def test_nested_children(self):
        """Tests a list with multiple levels of nesting."""
        # 1 -> 2
        # |
        # 3 -> 4
        #      |
        #      5
        n1 = MultiLevelListNode(1)
        n2 = MultiLevelListNode(2)
        n3 = MultiLevelListNode(3)
        n4 = MultiLevelListNode(4)
        n5 = MultiLevelListNode(5)

        n1.next = n2
        n1.child = n3
        n3.next = n4
        n4.child = n5

        flattened = self.solution.flatten(n1)
        # Expected order based on logic: 1 -> 2 -> 3 -> 4 -> 5
        self.assertEqual(self.get_list_values(flattened), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
