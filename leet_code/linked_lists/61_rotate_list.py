"""
Problem: Rotate List - rotate a linked list to the right by k places

Approach:
- Find the length of the list and connect the tail to head (make it circular)
- Calculate effective rotations (k % n) to handle k > n
- Find the new tail at position (n - k - 1) from the head
- Break the circle at the new tail to form the rotated list
- Time complexity: O(n) where n is the number of nodes
- Space complexity: O(1) - only using pointers
"""

import unittest
from typing import Optional


class ListNode:
    """Definition for singly-linked list node."""

    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    """Solution for LeetCode 61: Rotate List."""

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the list to the right by k places.

        For example, rotating [1,2,3,4,5] by k=2 gives [4,5,1,2,3].
        """
        # Edge case: empty list or single node
        if not head or not head.next:
            return head

        # Find the tail and count nodes
        old_tail = head
        n = 1

        while old_tail.next:
            old_tail = old_tail.next
            n += 1

        # Make the list circular by connecting tail to head
        old_tail.next = head

        # Find the new tail: it's at position (n - k - 1) from head
        new_tail = head
        k = k % n  # Handle k > n by taking modulo

        for _ in range(n - k - 1):
            new_tail = new_tail.next

        # Break the circle at new_tail
        new_head = new_tail.next
        new_tail.next = None

        return new_head


class TestRotateList(unittest.TestCase):
    """Test cases for Rotate List solution."""

    def setUp(self):
        self.solution = Solution()

    def list_to_array(self, head: Optional[ListNode]) -> list[int]:
        """Helper function to convert linked list to array."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def array_to_list(self, arr: list[int]) -> Optional[ListNode]:
        """Helper function to convert array to linked list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def test_basic_rotation(self):
        """Test basic rotation: [1,2,3,4,5], k=2 -> [4,5,1,2,3]."""
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.rotateRight(head, 2)
        expected = [4, 5, 1, 2, 3]
        self.assertEqual(self.list_to_array(result), expected)

    def test_single_rotation(self):
        """Test single rotation: [0,1,2], k=1 -> [2,0,1]."""
        head = self.array_to_list([0, 1, 2])
        result = self.solution.rotateRight(head, 1)
        expected = [2, 0, 1]
        self.assertEqual(self.list_to_array(result), expected)

    def test_full_rotation(self):
        """Test full rotation (k equals length): [1,2,3], k=3 -> [1,2,3]."""
        head = self.array_to_list([1, 2, 3])
        result = self.solution.rotateRight(head, 3)
        expected = [1, 2, 3]
        self.assertEqual(self.list_to_array(result), expected)

    def test_k_greater_than_length(self):
        """Test k > length: [1,2], k=5 -> [2,1] (same as k=1)."""
        head = self.array_to_list([1, 2])
        result = self.solution.rotateRight(head, 5)
        expected = [2, 1]
        self.assertEqual(self.list_to_array(result), expected)

    def test_zero_rotation(self):
        """Test zero rotation: [1,2,3], k=0 -> [1,2,3]."""
        head = self.array_to_list([1, 2, 3])
        result = self.solution.rotateRight(head, 0)
        expected = [1, 2, 3]
        self.assertEqual(self.list_to_array(result), expected)

    def test_single_node(self):
        """Test single node list: [1], k=1 -> [1]."""
        head = self.array_to_list([1])
        result = self.solution.rotateRight(head, 1)
        expected = [1]
        self.assertEqual(self.list_to_array(result), expected)

    def test_empty_list(self):
        """Test empty list."""
        head = None
        result = self.solution.rotateRight(head, 5)
        self.assertIsNone(result)

    def test_two_nodes_rotate_once(self):
        """Test two nodes, rotate once: [1,2], k=1 -> [2,1]."""
        head = self.array_to_list([1, 2])
        result = self.solution.rotateRight(head, 1)
        expected = [2, 1]
        self.assertEqual(self.list_to_array(result), expected)

    def test_large_rotation(self):
        """Test with large k: [1,2,3,4], k=10 -> [3,4,1,2] (k%4=2)."""
        head = self.array_to_list([1, 2, 3, 4])
        result = self.solution.rotateRight(head, 10)
        expected = [3, 4, 1, 2]
        self.assertEqual(self.list_to_array(result), expected)

    def test_rotate_to_last_position(self):
        """Test rotating to last position: [1,2,3,4,5], k=4 -> [2,3,4,5,1]."""
        head = self.array_to_list([1, 2, 3, 4, 5])
        result = self.solution.rotateRight(head, 4)
        expected = [2, 3, 4, 5, 1]
        self.assertEqual(self.list_to_array(result), expected)


if __name__ == "__main__":
    unittest.main()
