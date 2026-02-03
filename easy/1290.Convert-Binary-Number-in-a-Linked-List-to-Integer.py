"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is
either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
The most significant bit is at the head of the linked list.

Example 1:
1 -> 0 -> 1
Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:
Input: head = [0]
Output: 0

Constraints:
The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.

Hint 1
Traverse the linked list and store all values in a string or array. convert the values obtained to decimal value.

Hint 2
You can solve the problem in O(1) memory using bits operation. use shift left operation ( << ) and or operation
( | ) to get the decimal value in one operation.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity: O(n)
# Space complexity: O(n)
def getDecimalValue(head: Optional[ListNode]) -> int:
    number = ""
    current = head
    while current:
        number += str(current.val)
        current = current.next

    return int(number, 2)


# Time complexity: O(n)
# Space complexity: O(1)
def getDecimalValue1(head: Optional[ListNode]) -> int:
    number = 0
    current = head
    while current:
        number = (number << 1) | current.val
        current = current.next

    return number


assert getDecimalValue(ListNode(1, ListNode(0, ListNode(1)))) == 5
assert getDecimalValue(ListNode(0)) == 0
assert getDecimalValue(ListNode(1, ListNode(0, ListNode(0, ListNode(1, ListNode(0, ListNode(0, ListNode(1)))))))) == 73
