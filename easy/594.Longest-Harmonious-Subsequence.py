""" #TODO example
594. Longest Harmonious Subsequence
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:
Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation:
The longest harmonious subsequence is [3,2,2,2,3].

Example 2:
Input: nums = [1,2,3,4]
Output: 2
Explanation:
The longest harmonious subsequences are [1,2], [2,3], and [3,4], all of which have a length of 2.

Example 3:
Input: nums = [1,1,1,1]
Output: 0
Explanation:
No harmonic subsequence exists.

Constraints:
1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""
from typing import List


def findLHS(nums: List[int]) -> int:
    #     if len(set(nums)) == 1:
    #         return 0
    #     d = defaultdict(int)
    #     for i in nums:
    #         d[i] += 1
    #     r = 0
    #     for n in d:
    #         if n+1 in d:
    #             r = max(r, d[n] + d[n+1])
    #
    #     return r
    nums.sort()
    l, r = 0, 1
    length = 0
    while r < len(nums):
        diff = nums[r] - nums[l]
        if diff == 1:
            length = max(length, r - l + 1)
        if diff <= 1:
            r += 1
        else:
            l += 1

    return length


assert findLHS([1, 3, 2, 2, 5, 2, 3, 7]) == 5
assert findLHS([1, 2, 3, 4]) == 2
assert findLHS([1, 1, 1, 1]) == 0
assert findLHS([1, 3, 5, 7, 9, 11, 13, 15, 17]) == 0
assert findLHS([1, 4, 1, 3, 1, -14, 1, -13]) == 2
