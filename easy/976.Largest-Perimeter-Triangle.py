"""
976. Largest Perimeter Triangle

Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three
of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5
Explanation: You can form a triangle with three side lengths: 1, 2, and 2.

Example 2:
Input: nums = [1,2,1,10]
Output: 0
Explanation:
You cannot use the side lengths 1, 1, and 2 to form a triangle.
You cannot use the side lengths 1, 1, and 10 to form a triangle.
You cannot use the side lengths 1, 2, and 10 to form a triangle.
As we cannot use any three side lengths to form a triangle of non-zero area, we return 0.


Constraints:
3 <= nums.length <= 104
1 <= nums[i] <= 106
"""
import heapq
from typing import List


# Time complexity: O(n log n)
# Space complexity: O(n)
def largestPerimeter(nums: List[int]) -> int:
    nums = sorted(nums)

    for i in range(len(nums) - 1, 1, -1):
        if nums[i - 2] + nums[i - 1] > nums[i]:
            return nums[i - 2] + nums[i - 1] + nums[i]

    return 0


# Time complexity: O(n log n)
# Space complexity: O(1)
def largestPerimeter1(nums: List[int]) -> int:
    heapq._heapify_max(nums)
    biggest = heapq._heappop_max(nums)
    second = heapq._heappop_max(nums)
    while len(nums) > 0:
        smallest = heapq._heappop_max(nums)
        if smallest + second > biggest:
            return smallest + second + biggest
        biggest = second
        second = smallest

    return 0


assert largestPerimeter([2, 1, 2]) == 5
assert largestPerimeter([2, 1, 1]) == 0
assert largestPerimeter([1, 2, 1, 10]) == 0
assert largestPerimeter([3, 2, 3, 4]) == 10
