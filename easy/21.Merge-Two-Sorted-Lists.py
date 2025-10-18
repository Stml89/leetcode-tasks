"""
21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
1 -> 2 -> 4
1 -> 3 -> 4
1 -> 1 -> 2 -> 3 -> 4 -> 4
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(m + n)
# Space complexity: O(m + n)
def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 and not list2:
        return

    if not list1:
        return list2

    if not list2:
        return list1

    current_list = ListNode()
    p_head = current_list
    while list1 and list2:
        l1v = list1.val if list1 else None
        l2v = list2.val if list2 else None
        if l1v <= l2v:
            current_list.next = ListNode(val=l1v)
            current_list = current_list.next
            list1 = list1.next
        else:
            current_list.next = ListNode(val=l2v)
            current_list = current_list.next
            list2 = list2.next

    if list1:
        current_list.next = list1

    if list2:
        current_list.next = list2

    return p_head.next


a3 = ListNode(val=5)
a2 = ListNode(val=3, next=a3)
a1 = ListNode(val=1, next=a2)

b3 = ListNode(val=4)
b2 = ListNode(val=2, next=b3)
b1 = ListNode(val=1, next=b2)

mergeTwoLists(a3, b1)
