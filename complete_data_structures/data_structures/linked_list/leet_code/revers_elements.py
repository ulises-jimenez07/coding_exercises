'''
Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):

    def reverseList(self, head):
        dummy =  ListNode(-1)
        prev = None
        dummy.next = head
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        return prev