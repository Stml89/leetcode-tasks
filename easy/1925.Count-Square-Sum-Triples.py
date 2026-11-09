"""
1925. Count Square Sum Triples

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.
Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

Example 1:
Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:
Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).
 

Constraints:
1 <= n <= 250

Hint 1
Iterate over all possible pairs (a,b) and check that the square root of a * a + b * b is an integers less than or equal n

Hint 2
You can check that the square root of an integer is an integer using binary seach or a builtin function like sqrt
"""

from math import isqrt


# Time Complexity: O(n^2)
# Space Complexity: O(1)
def countTriples(n: int) -> int:
    result = 0

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            c_squared = a * a + b * b
            c = isqrt(c_squared)

            if c <= n and c * c == c_squared:
                result += 1

    return result


# Time Complexity: O(n²)
# Space Complexity: O(n)
def countTriples1(n: int) -> int:
    squares = {i * i for i in range(1, n + 1)}
    result = 0

    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a * a + b * b in squares:
                result += 1

    return result


assert countTriples(1) == 0
assert countTriples(2) == 0
assert countTriples(3) == 0
assert countTriples(4) == 0
assert countTriples(5) == 2
assert countTriples(10) == 4
assert countTriples(12) == 4
assert countTriples(13) == 6
assert countTriples(15) == 8
assert countTriples(20) == 12
