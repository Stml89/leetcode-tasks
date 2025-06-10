"""
643. Maximum Average Subarray I
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

Constraints:
n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
# TODO
from typing import List


def findMaxAverage(nums: List[int], k: int) -> float:
    if len(nums) == k:
        return sum(nums) / k
    start, m_avg = 0, 0
    while start + k <= len(nums):
        s = sum(nums[start:k + start]) / k
        if m_avg < s:
            m_avg = s
        start += 1
    return m_avg


assert findMaxAverage([1, 12, -5, -6, 50, 3], k=4) == 12.75000
assert findMaxAverage([5], k=1) == 5.00000
