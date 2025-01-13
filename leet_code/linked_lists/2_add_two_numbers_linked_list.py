from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Adds two non-empty linked lists representing non-negative integers (digits least significant first)
        and returns the sum as a linked list.

        Args:
            l1: The first non-empty linked list.
            l2: The second non-empty linked list.

        Returns:
            The linked list representing the sum of l1 and l2.
        """

        dummy = head = ListNode(0)  # Create a dummy head node
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum = val1 + val2 + carry

            carry = sum // 10
            head.next = ListNode(sum % 10)
            head = head.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next  # Return the actual list (skip dummy head)


# Test Cases (enhanced with edge cases and clarity)
def test_addTwoNumbers():
    solution = Solution()

    # Test case 1: Basic addition with no carryover
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    expected = ListNode(7, ListNode(0, ListNode(8)))
    assert solution.addTwoNumbers(l1, l2) == expected

    # Test case 2: Addition with carryover (all digits)
    l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))
    l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
    expected = ListNode(
        8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(1)))))
    )
    assert solution.addTwoNumbers(l1, l2) == expected

    # Test case 3: Lists with different lengths (longer l1)
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6))
    expected = ListNode(7, ListNode(0, ListNode(4)))
    assert solution.addTwoNumbers(l1, l2) == expected

    # Test case 4: Lists with different lengths (longer l2)
    l1 = ListNode(5)
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    expected = ListNode(0, ListNode(1, ListNode(5)))
    assert solution.addTwoNumbers(l1, l2) == expected

    # Test case 5: Empty lists
    l1 = None
    l2 = None
    expected = None
    assert solution.addTwoNumbers(l1, l2) == expected

    # Test case 6: Single-digit lists
    l1 = ListNode(1)
    l2 = ListNode(9)
    expected = ListNode(0, ListNode(1))
    assert solution.addTwoNumbers(l1, l2) == expected


print("All test cases passed!")
