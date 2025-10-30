"""
977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of
each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n)
solution using a different approach?
"""
from typing import List


# Time complexity: O(n log n)
# Space complexity: O(n)
def sortedSquares(nums: List[int]) -> List[int]:
    return sorted([item ** 2 for item in nums])


# Time complexity: O(n)
# Space complexity: O(n)
def sortedSquares1(nums: List[int]) -> List[int]:
    res = []
    beginning, end = 0, len(nums) - 1

    while beginning <= end:
        beginning_num = nums[beginning] ** 2
        end_num = nums[end] ** 2
        if beginning_num > end_num:
            res.append(beginning_num)
            beginning += 1
        else:
            res.append(end_num)
            end -= 1

    return res[::-1]


assert sortedSquares([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
assert sortedSquares([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]
