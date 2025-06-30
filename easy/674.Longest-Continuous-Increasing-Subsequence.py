"""
674. Longest Continuous Increasing Subsequence

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence
(i.e. subarray). The subsequence must be strictly increasing.
A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1],
..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Example 1:
Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.

Example 2:
Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

Constraints:
1 <= nums.length <= 104
-109 <= nums[i] <= 109
"""
from typing import List


def findLengthOfLCIS(nums: List[int]) -> int:
    # if not nums:
    #     return 0
    #
    # if len(set(nums)) == 1:
    #     return 1
    #
    # prev = count = indx = max_count = 0
    #
    # while indx <= len(nums) - 1:
    #     if nums[indx] <= prev:
    #         max_count = max(max_count, count)
    #         count = 0
    #     count += 1
    #     prev = nums[indx]
    #     indx += 1
    #
    # return max(max_count, count)
    max_count = 1
    count = 1

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            count += 1
        else:
            count = 1
        max_count = max(max_count, count)
    return max_count


assert findLengthOfLCIS([1, 3, 5, 4, 7]) == 3
assert findLengthOfLCIS([2, 2, 2, 2, 2]) == 1
assert findLengthOfLCIS([1, 2, 3, 4, 5]) == 5
assert findLengthOfLCIS([]) == 0
assert findLengthOfLCIS([1, 0]) == 1
assert findLengthOfLCIS([1, 3, 5, 4, 2, 3, 4, 5]) == 4
assert findLengthOfLCIS([1, 1, 2]) == 2
