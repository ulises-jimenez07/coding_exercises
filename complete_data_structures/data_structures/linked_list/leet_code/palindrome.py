"""
Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    # Alternative implementation using set (kept for reference)
    # def is_palindrome_set(self, head):
    #     vals = set()
    #     curr = head
    #     if head is None:
    #         return False
    #
    #     while curr:
    #         if curr.val in vals:
    #             vals.remove(curr.val)
    #         else:
    #             vals.add(curr.val)
    #         curr = curr.next
    #     return len(vals) < 2

    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
