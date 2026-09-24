"""
1800. Maximum Ascending Subarray Sum

Given an array of positive integers nums, return the maximum possible sum of an strictly increasing subarray in nums.
A subarray is defined as a contiguous sequence of numbers in an array.

Example 1:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.

Example 2:
Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.

Example 3:
Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Hint 1
It is fast enough to check all possible subarrays
Hint 2
The end of each ascending subarray will be the start of the next
"""
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(1)
def maxAscendingSum(nums: List[int]) -> int:
    max_sum = float('-inf')
    prev = nums[0]
    curr_sum = nums[0]

    for i in nums[1:]:
        if i > prev:
            curr_sum += i
            prev = i
        else:
            prev = 0
            curr_sum = i

        max_sum = max(max_sum, curr_sum)

    return max_sum


assert maxAscendingSum([10, 20, 30, 5, 10, 50]) == 65
assert maxAscendingSum([10, 20, 30, 40, 50]) == 150
assert maxAscendingSum([12, 17, 15, 13, 10, 11, 12]) == 33
