import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        """Initializes a ListNode object."""
        self.val = x
        self.next = None


class Solution:
    """
    Contains the solution for finding the intersection node of two linked lists.
    """

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        Finds the node at which the intersection of two singly linked lists begins.

        Args:
            headA: The head node of the first linked list.
            headB: The head node of the second linked list.

        Returns:
            The intersecting node if one exists, otherwise None.
        """

        # Helper function to calculate the length of a linked list.
        def find_length(head):
            length = 0
            curr = head
            while curr:
                length += 1
                curr = curr.next
            return length

        # Calculate the lengths of both lists.
        n = find_length(headA)
        m = find_length(headB)

        # Initialize pointers to the heads of the lists.
        currA = headA
        currB = headB

        # Align the starting points of the pointers.
        # Move the pointer of the longer list forward by the difference in lengths.
        # This ensures both pointers are equidistant from the potential intersection point.
        if n <= m:
            for _ in range(m - n):
                # Check if currB becomes None during alignment (can happen if lengths are miscalculated or lists are strange)
                if currB is None:
                    return None  # Should not happen with valid inputs if lengths are correct
                currB = currB.next
        else:  # n > m
            for _ in range(n - m):
                # Check if currA becomes None during alignment
                if currA is None:
                    return None  # Should not happen with valid inputs if lengths are correct
                currA = currA.next

        # Traverse both lists simultaneously.
        while currA and currB:  # Iterate as long as both pointers are valid
            # If the pointers point to the same node object, we've found the intersection.
            if currA == currB:
                return currA
            # Move both pointers one step forward.
            currA = currA.next
            currB = currB.next

        # If the loop finishes without finding an intersection, return None.
        return None


# --- Unit Tests ---
class TestGetIntersectionNode(unittest.TestCase):

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
        headA, headB, intersection_node = self.create_intersecting_lists(
            [4, 1], [5, 6, 1], [8, 4, 5]
        )
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, intersection_node)
        self.assertEqual(result.val, 8)

    def test_no_intersection(self):
        # List A: 2 -> 6 -> 4
        # List B: 1 -> 5
        headA = self.create_linked_list([2, 6, 4])
        headB = self.create_linked_list([1, 5])
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_one_list_empty(self):
        headA = self.create_linked_list([1, 2, 3])
        headB = None
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)
        result = sol.getIntersectionNode(headB, headA)
        self.assertIsNone(result)

    def test_both_lists_empty(self):
        headA = None
        headB = None
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_intersection_at_head(self):
        # List A: 1 -> 2 -> 3
        # List B: 1 -> 2 -> 3 (same list)
        headA, headB, intersection_node = self.create_intersecting_lists(
            [], [], [1, 2, 3]
        )
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, intersection_node)
        self.assertEqual(result.val, 1)

    def test_different_lengths_intersection(self):
        # List A: 3 -> 7 -> 8 -> 10
        # List B: 99 -> 1 -> 8 -> 10
        # Intersection: 8 -> 10
        headA, headB, intersection_node = self.create_intersecting_lists(
            [3, 7], [99, 1], [8, 10]
        )
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, intersection_node)
        self.assertEqual(result.val, 8)

    def test_different_lengths_no_intersection(self):
        headA = self.create_linked_list([1, 2, 3, 4])
        headB = self.create_linked_list([5, 6])
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertIsNone(result)

    def test_intersection_is_single_node(self):
        # List A: 1 -> 9 -> 1 -> 2 -> 4
        # List B: 3 -> 2 -> 4
        # Intersection: 2 -> 4
        headA, headB, intersection_node = self.create_intersecting_lists(
            [1, 9, 1], [3], [2, 4]
        )
        sol = Solution()
        result = sol.getIntersectionNode(headA, headB)
        self.assertEqual(result, intersection_node)
        self.assertEqual(result.val, 2)


if __name__ == "__main__":
    unittest.main()
