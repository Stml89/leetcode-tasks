"""
1827. Minimum Operations to Make the Array Increasing

You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.
-- For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

Example 1:
Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].

Example 2:
Input: nums = [1,5,2,4,1]
Output: 14

Example 3:
Input: nums = [8]
Output: 0


Constraints:
1 <= nums.length <= 5000
1 <= nums[i] <= 104

Hint 1
nums[i+1] must be at least equal to nums[i] + 1.

Hint 2
Think greedily. You don't have to increase nums[i+1] beyond nums[i]+1.

Hint 3
Iterate on i and set nums[i] = max(nums[i-1]+1, nums[i]) .
"""
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def minOperations(nums: List[int]) -> int:
    operations = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            needed = nums[i - 1] + 1 - nums[i]
            operations += needed
            nums[i] = nums[i - 1] + 1

    return operations


# Time Complexity: O(n)
# Space Complexity: O(1)
def minOperations(nums: list[int]) -> int:
    operations = 0
    prev = nums[0]

    for i in range(1, len(nums)):
        current = max(nums[i], prev + 1)
        operations += current - nums[i]
        prev = current

    return operations


assert minOperations([1, 1, 1]) == 3
assert minOperations([1, 5, 2, 4, 1]) == 14
assert minOperations([8]) == 0
