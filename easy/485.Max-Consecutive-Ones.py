"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
from typing import List


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_seq = 0
    tmp_count = 0
    for i in nums:
        if i == 1:
            tmp_count += 1
        else:
            max_seq = max(tmp_count, max_seq)
            tmp_count = 0

    return max(tmp_count, max_seq)


assert findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
