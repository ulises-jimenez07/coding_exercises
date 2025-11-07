"""
Remove Duplicates
Given the head of a sorted linked list,
delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head

        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next

        return dummy.next
