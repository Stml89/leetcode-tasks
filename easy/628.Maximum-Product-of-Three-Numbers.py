""" # TODO example
628. Maximum Product of Three Numbers
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:
3 <= nums.length <= 104
-1000 <= nums[i] <= 1000
"""
import heapq
from typing import List


def maximumProduct(nums: List[int]) -> int:
    if not nums:
        return 0

    # nums.sort()
    # return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
    max1, max2, max3 = heapq.nlargest(3, nums)
    min1, min2 = heapq.nsmallest(2, nums)

    return max(max1 * max2 * max3, min1 * min2 * max1)


assert maximumProduct([1, 2, 3]) == 6
assert maximumProduct([1, 2, 3, 4]) == 24
assert maximumProduct([-1, -2, -3]) == -6
assert maximumProduct([-100, -98, -1, 2, 3, 4]) == 39200
