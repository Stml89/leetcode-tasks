"""
1399. Count Largest Group

You are given an integer n.
We need to group the numbers from 1 to n according to the sum of its digits. For example, the numbers 14 and 5
belong to the same group, whereas 13 and 3 belong to different groups.
Return the number of groups that have the largest size, i.e. the maximum number of elements.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Constraints:
1 <= n <= 104

Hint 1
Count the digit sum for each integer in the range and find out the largest groups.
"""
from collections import defaultdict


# Time complexity: O(n * log n)
# Space complexity: O(log n)
def countLargestGroup(n: int) -> int:
    groups = {}

    for num in range(1, n + 1):
        digit_sum = sum(int(digit) for digit in str(num))
        groups[digit_sum] = groups.get(digit_sum, 0) + 1

    max_size = max(groups.values())
    return sum(1 for size in groups.values() if size == max_size)


# Time complexity: O(n * d), where n is the input number and d is the number of digits in the largest number
# Space complexity: O(log n)
def countLargestGroup1(n: int) -> int:
    groups = defaultdict(int)

    for i in range(1, n + 1):
        s = sum(map(int, str(i)))
        groups[s] += 1

    max_size = max(groups.values())

    return sum(1 for v in groups.values() if v == max_size)


assert countLargestGroup(13) == 4
assert countLargestGroup(2) == 2
