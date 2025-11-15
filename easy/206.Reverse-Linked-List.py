"""
206. Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    rev = ListNode(val=head.val)
    head = head.next
    while head:
        rev = ListNode(val=head.val, next=rev)
        head = head.next

    return rev


ln1_input = ListNode(val=1, next=ListNode(val=2, next=ListNode(val=3, next=ListNode(val=4, next=ListNode(val=5)))))
ln1_output = ListNode(val=5, next=ListNode(val=4, next=ListNode(val=3, next=ListNode(val=2, next=ListNode(val=1)))))
assert reverseList(ln1_input) == ln1_output

ln2_input = ListNode(val=1, next=ListNode(val=2))
ln2_output = ListNode(val=2, next=ListNode(val=1))
assert reverseList(ln2_input) == ln2_output

ln3_input = ListNode()
ln3_output = ListNode()
assert reverseList(ln3_input) == ln3_output
