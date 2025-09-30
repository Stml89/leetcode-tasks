"""
896. Monotonic Array

An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.

Example 1:
Input: nums = [1,2,2,3]
Output: true

Example 2:
Input: nums = [6,5,4,4]
Output: true

Example 3:
Input: nums = [1,3,2]
Output: false


Constraints:
1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""
from itertools import pairwise
from typing import List


def isMonotonic(nums: List[int]) -> bool:
    flag = 0
    for i in range(1, len(nums)):
        if nums[i - 1] < nums[i]:
            if flag == -1:
                return False
            flag = 1
        elif nums[i - 1] > nums[i]:
            if flag == 1:
                return False
            flag = -1

    return True


def isMonotonic1(nums: List[int]) -> bool:
    is_inc = all(a <= b for a, b in pairwise(nums))
    is_dec = all(a >= b for a, b in pairwise(nums))

    return is_inc or is_dec


def isMonotonic2(nums: List[int]) -> bool:
    def inc(nums: List[int]) -> bool:
        prev = float('-inf')
        for num in nums:
            if num < prev:
                return False
            prev = num
        return True

    def dec(nums: List[int]) -> bool:
        prev = float('inf')
        for num in nums:
            if num > prev:
                return False
            prev = num
        return True

    return inc(nums) or dec(nums)


assert isMonotonic([1, 2, 2, 3])
assert isMonotonic([6, 5, 4, 4])
assert not isMonotonic([1, 3, 2])
assert not isMonotonic([1, 2, 1])
assert isMonotonic([1, 2, 4, 5])
