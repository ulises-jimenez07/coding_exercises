"""
Remove Linked List Elements
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy
        curr_node = head

        while curr_node:
            if curr_node.val == val:
                prev_node.next = curr_node.next
            else:
                prev_node = curr_node
            curr_node = curr_node.next

        return dummy.next
