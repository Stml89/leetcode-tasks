"""
1952. Three Divisors

Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
An integer m is a divisor of n if there exists an integer k such that n = k * m.

Example 1:
Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:
Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.

Constraints:
1 <= n <= 104

Hint 1
You can count the number of divisors and just check that they are 3
Hint 2
Beware of the case of n equal 1 as some solutions might fail in it
"""
from math import isqrt


# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)
def isThree(n: int) -> bool:
    root = isqrt(n)

    if root * root != n:
        return False

    if root < 2:
        return False

    for i in range(2, isqrt(root) + 1):
        if root % i == 0:
            return False

    return True


# Time Complexity: O(n)
# Space Complexity: O(1)
def isThree1(n: int) -> bool:
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

            if count > 3:
                return False

    return count == 3


assert isThree(2) is False
assert isThree(4) is True
assert isThree(9) is True
assert isThree(16) is False
assert isThree(1) is False
assert isThree(25) is True
assert isThree(36) is False
assert isThree(49) is True
assert isThree(100) is False
