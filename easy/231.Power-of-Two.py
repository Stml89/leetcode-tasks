"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.

Example 1:
Input: n = 1
Output: true
Explanation: 20 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 24 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


# Time complexity: O(1)
# Space complexity: O(1)
def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0


# Time complexity: O(1)
# Space complexity: O(1)
def isPowerOfTwo1(n: int) -> bool:
    return n >= 0 and n.bit_count() == 1


# Time complexity: O(log n)
# Space complexity: O(1)
def isPowerOfTwo2(n: int) -> bool:
    if n <= 0:
        return False

    x = 1
    while x < n:
        x *= 2
    return x == n


# Time complexity: O(1)
# Space complexity: O(1)
def isPowerOfTwo3(n: int) -> bool:
    return n > 0 and ((1 << 30) % n) == 0


assert isPowerOfTwo(1) == True
assert isPowerOfTwo(2) == True
assert isPowerOfTwo(3) == False
assert isPowerOfTwo(16) == True
