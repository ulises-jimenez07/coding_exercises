from typing import Optional, List
import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node of a singly linked list.
        If there are two middle nodes (i.e., an even number of nodes),
        it returns the second middle node.

        This method uses the "slow and fast pointer" technique.
        - The `slow` pointer moves one step at a time.
        - The `fast` pointer moves two steps at a time.
        When the `fast` pointer reaches the end of the list (or goes beyond it),
        the `slow` pointer will be at the middle node.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next  # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps

        # When the loop ends, slow pointer is at the middle node
        return slow


# Helper function to create a linked list from a list of values
def create_linked_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head_node = ListNode(vals[0])
    current = head_node
    for val in vals[1:]:
        current.next = ListNode(val)
        current = current.next
    return head_node


# Helper function to convert a linked list (from a given node) to a list of values
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    vals = []
    current = node
    while current:
        vals.append(current.val)
        current = current.next
    return vals


class TestMiddleNode(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        head = None
        self.assertIsNone(self.solution.middleNode(head))

    def test_single_node_list(self):
        head = create_linked_list([1])
        self.assertEqual(linked_list_to_list(self.solution.middleNode(head)), [1])

    def test_even_number_of_nodes(self):
        head = create_linked_list([1, 2, 3, 4])  # Middle should be 3, so [3,4]
        self.assertEqual(linked_list_to_list(self.solution.middleNode(head)), [3, 4])

    def test_odd_number_of_nodes(self):
        head = create_linked_list([1, 2, 3, 4, 5])  # Middle should be 3, so [3,4,5]
        self.assertEqual(linked_list_to_list(self.solution.middleNode(head)), [3, 4, 5])

    def test_longer_even_list(self):
        head = create_linked_list([1, 2, 3, 4, 5, 6])  # Middle should be 4, so [4,5,6]
        self.assertEqual(linked_list_to_list(self.solution.middleNode(head)), [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
