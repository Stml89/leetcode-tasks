"""
203. Remove Linked List Elements
Solved
Easy
Topics
Companies
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    dummy = ListNode(next=head)
    prev_node = dummy
    current_node = head

    while current_node:
        if current_node.val == val:
            prev_node.next = current_node.next
        else:
            prev_node = current_node
        current_node = current_node.next

    return dummy.next


a4 = ListNode(2)
a3 = ListNode(5, a4)
a2 = ListNode(2, a3)
a1 = ListNode(1, a2)

removeElements(a1, 2)
