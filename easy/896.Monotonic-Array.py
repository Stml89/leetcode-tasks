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


assert isMonotonic([1, 2, 2, 3])
assert isMonotonic([6, 5, 4, 4])
assert not isMonotonic([1, 3, 2])
assert not isMonotonic([1, 2, 1])
assert isMonotonic([1, 2, 4, 5])
