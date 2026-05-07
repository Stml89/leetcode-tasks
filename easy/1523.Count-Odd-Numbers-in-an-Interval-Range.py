"""
1523. Count Odd Numbers in an Interval Range

Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
0 <= low <= high <= 10^9

Hint 1
If the range (high - low + 1) is even, the number of even and odd numbers in this range will be the same.

Hint 2
If the range (high - low + 1) is odd, the solution will depend on the parity of high and low.
"""


# Time complexity: O(1)
# Space complexity: O(1)
def countOdds(low: int, high: int) -> int:
    if (high - low + 1) % 2 == 0:
        return (high - low + 1) // 2

    if high % 2 == 0 and low % 2 == 0:
        return (high - low) // 2

    return (high - low) // 2 + 1


assert countOdds(3, 7) == 3
assert countOdds(8, 10) == 1
