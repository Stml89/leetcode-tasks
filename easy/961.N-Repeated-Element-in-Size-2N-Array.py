"""
961. N-Repeated Element in Size 2N Array

You are given an integer array nums with the following properties:
- nums.length == 2 * n.
- nums contains n + 1 unique elements.
- Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5

Constraints:
2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
"""
from collections import Counter
from typing import List


# Time complexity: O(N)
# Space complexity: O(N)
def repeatedNTimes1(nums: List[int]) -> int:
    mc = Counter(nums).most_common()
    n = len(nums) / 2
    for v, c in mc:
        if c == n:
            return v
    return 0


# Time complexity: O(N)
# Space complexity: O(N)
def repeatedNTimes(nums: list[int]) -> int:
    d = {}
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            return i


assert repeatedNTimes([1, 2, 3, 3]) == 3
assert repeatedNTimes([2, 1, 2, 5, 3, 2]) == 2
assert repeatedNTimes([5, 1, 5, 2, 5, 3, 5, 4]) == 5
