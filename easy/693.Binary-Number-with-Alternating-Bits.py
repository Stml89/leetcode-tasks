"""
693. Binary Number with Alternating Bits
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:
1 <= n <= 231 - 1
"""
def hasAlternatingBits(n: int) -> bool:
    b = "{0:b}".format(n)
    for i in range(1, len(b)):
        if b[i] == b[i - 1]:
            return False
    return True


assert hasAlternatingBits(5)
assert not hasAlternatingBits(7)
assert not hasAlternatingBits(11)
