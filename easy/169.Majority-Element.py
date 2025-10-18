"""
169. Majority Element

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
from collections import defaultdict
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def majorityElement(nums: List[int]) -> int:
    majority_el = len(nums) // 2
    d = defaultdict(int)
    for i in nums:
        d[i] += 1

    for k, v in list(d.items()):
        if v > majority_el:
            return k


# Time complexity: O(n log n)
# Space complexity: O(log n)
def majorityElement1(nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    return nums[n // 2]


# Time complexity: O(n)
# Space complexity: O(n)
def majorityElement2(nums: List[int]) -> int:
    counts = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > len(nums) // 2:
            return num


assert majorityElement([6, 5, 5]) == 5
assert majorityElement([3, 2, 3]) == 3
assert majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
