"""
1005. Maximize Sum Of Array After K Negations

Given an integer array nums and an integer k, modify the array in the following way:
- choose an index i and replace nums[i] with -nums[i].

You should apply this process exactly k times. You may choose the same index i multiple times.
Return the largest possible sum of the array after modifying it in this way.

Example 1:
Input: nums = [4,2,3], k = 1
Output: 5
Explanation: Choose index 1 and nums becomes [4,-2,3].

Example 2:
Input: nums = [3,-1,0,2], k = 3
Output: 6
Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].

Example 3:
Input: nums = [2,-3,-1,5,-4], k = 2
Output: 13
Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].

Constraints:
1 <= nums.length <= 104
-100 <= nums[i] <= 100
1 <= k <= 104
"""
import heapq
from typing import List


# Time complexity: O(n log n)
# Space complexity: O(1)
def largestSumAfterKNegations(nums: List[int], k: int) -> int:
    nums.sort()
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1

    if k % 2 != 0:
        nums.sort()
        nums[0] = -nums[0]

    return sum(nums)


assert largestSumAfterKNegations(nums=[4, 2, 3], k=1) == 5
assert largestSumAfterKNegations(nums=[3, -1, 0, 2], k=3) == 6
assert largestSumAfterKNegations(nums=[2, -3, -1, 5, -4], k=2) == 13
assert largestSumAfterKNegations(nums=[-100, -100, -100], k=4) == 100
assert largestSumAfterKNegations(nums=[-2, 5, 0, 2, -2], k=3) == 11
