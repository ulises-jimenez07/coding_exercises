"""
Problem: Find the node where two linked lists intersect

Approach 1: Length Calculation
- Calculate lengths of both lists
- Align the starting points by advancing the longer list
- Move both pointers until they meet at intersection
- Time complexity: O(n + m)
- Space complexity: O(1)

Approach 2: Two-Pointer Redirection (Cycle-like Alignment)
- Traverse both lists with two pointers
- When a pointer reaches the end, redirect it to the head of the other list
- If an intersection exists, they will meet after at most n + m steps
- Time complexity: O(n + m)
- Space complexity: O(1)
"""

import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    """
    Definition for a singly-linked list node.
    """

    def __init__(self, x):
        """Initializes a ListNode object."""
        self.val = x
        self.next = None


class Solution:
    """
    Contains the solution for finding the intersection node of two linked lists.
    """

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds the node at which the intersection of two singly linked lists begins.
        Uses the length calculation approach.
        """

        def find_length(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length

        n = find_length(headA)
        m = find_length(headB)

        currA = headA
        currB = headB

        # Align starting points by advancing longer list
        if n <= m:
            for _ in range(m - n):
                if currB is None:
                    return None
                currB = currB.next
        else:
            for _ in range(n - m):
                if currA is None:
                    return None
                currA = currA.next

        # Move both until intersection found
        while currA and currB:
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next

        return None

    def getIntersectionNodeOptimized(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds the node where two linked lists intersect using pointer redirection.
        """
        ptr_a, ptr_b = headA, headB

        # Continue until pointers meet (at intersection or both become None)
        while ptr_a != ptr_b:
            # If pointer reaches end, switch to other list's head
            # This balances the total distance traveled for both pointers
            ptr_a = ptr_a.next if ptr_a else headB
            ptr_b = ptr_b.next if ptr_b else headA

        return ptr_a


# --- Unit Tests ---
class TestGetIntersectionNode(unittest.TestCase):
    """
    Test suite for finding the intersection node of two linked lists.
    """

    def setUp(self):
        self.solution = Solution()

    def create_linked_list(self, values):
        """Helper function to create a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def create_intersecting_lists(self, listA_vals, listB_vals, common_vals):
        """Helper function to create two lists that intersect."""
        common_head = self.create_linked_list(common_vals)
        headA = self.create_linked_list(listA_vals)
        headB = self.create_linked_list(listB_vals)

        # Find the tails of listA and listB
        tailA = headA
        if tailA:
            while tailA.next:
                tailA = tailA.next

        tailB = headB
        if tailB:
            while tailB.next:
                tailB = tailB.next

        # Connect tails to the common part
        if tailA:
            tailA.next = common_head
        else:
            headA = common_head  # If listA was empty

        if tailB:
            tailB.next = common_head
        else:
            headB = common_head  # If listB was empty

        return headA, headB, common_head

    def test_intersection_exists(self):
        # List A: 4 -> 1 -> 8 -> 4 -> 5
        # List B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
        # Intersection: 8 -> 4 -> 5
        headA, headB, intersection_node = self.create_intersecting_lists([4, 1], [5, 6, 1], [8, 4, 5])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertEqual(result, intersection_node)
                self.assertEqual(result.val, 8)

    def test_no_intersection(self):
        # List A: 2 -> 6 -> 4
        # List B: 1 -> 5
        headA = self.create_linked_list([2, 6, 4])
        headB = self.create_linked_list([1, 5])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertIsNone(result)

    def test_one_list_empty(self):
        headA = self.create_linked_list([1, 2, 3])
        headB = None
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertIsNone(result)
                # Test symmetry (swapping heads)
                result = method(headB, headA)  # pylint: disable=arguments-out-of-order
                self.assertIsNone(result)

    def test_both_lists_empty(self):
        headA = None
        headB = None
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertIsNone(result)

    def test_intersection_at_head(self):
        # List A: 1 -> 2 -> 3
        # List B: 1 -> 2 -> 3 (same list)
        headA, headB, intersection_node = self.create_intersecting_lists([], [], [1, 2, 3])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertEqual(result, intersection_node)
                self.assertEqual(result.val, 1)

    def test_different_lengths_intersection(self):
        # List A: 3 -> 7 -> 8 -> 10
        # List B: 99 -> 1 -> 8 -> 10
        # Intersection: 8 -> 10
        headA, headB, intersection_node = self.create_intersecting_lists([3, 7], [99, 1], [8, 10])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertEqual(result, intersection_node)
                self.assertEqual(result.val, 8)

    def test_different_lengths_no_intersection(self):
        headA = self.create_linked_list([1, 2, 3, 4])
        headB = self.create_linked_list([5, 6])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertIsNone(result)

    def test_intersection_is_single_node(self):
        # List A: 1 -> 9 -> 1 -> 2 -> 4
        # List B: 3 -> 2 -> 4
        # Intersection: 2 -> 4
        headA, headB, intersection_node = self.create_intersecting_lists([1, 9, 1], [3], [2, 4])
        for method in [self.solution.getIntersectionNode, self.solution.getIntersectionNodeOptimized]:
            with self.subTest(method=method.__name__):
                result = method(headA, headB)
                self.assertEqual(result, intersection_node)
                self.assertEqual(result.val, 2)


if __name__ == "__main__":
    unittest.main()
