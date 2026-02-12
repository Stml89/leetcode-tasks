"""
1317. Convert Integer to the Sum of Two No-Zero Integers

No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.
Given an integer n, return a list of two integers [a, b] where:
- a and b are No-Zero integers.
- a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can return any of them.

Example 1:
Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.

Example 2:
Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.

Constraints:
2 <= n <= 104

Hint 1
Loop through all elements from 1 to n.

Hint 2
Choose A = i and B = n - i then check if A and B are both No-Zero integers.
"""
from typing import List


# Time complexity: O(n * log n)
# Space complexity: O(1)
def getNoZeroIntegers(n: int) -> List[int]:
    if n < 2:
        return []

    def is_no_zero_integer(num: int) -> bool:
        while num > 0:
            if num % 10 == 0:
                return False
            num //= 10
        return True

    for i in range(1, n):
        a = i
        b = n - i
        if is_no_zero_integer(a) and is_no_zero_integer(b):
            return [a, b]


assert getNoZeroIntegers(2) == [1, 1]
assert getNoZeroIntegers(11) == [2, 9]
