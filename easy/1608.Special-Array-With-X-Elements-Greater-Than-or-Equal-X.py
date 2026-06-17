"""
1608. Special Array With X Elements Greater Than or Equal X

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such
that there are exactly x numbers in nums that are greater than or equal to x.
Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special,
the value for x is unique.

Example 1:
Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

Example 2:
Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.

Example 3:
Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.

Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 1000

Hint 1
Count the number of elements greater than or equal to x for each x in the range [0, nums.length].

Hint 2
If for any x, the condition satisfies, return that x. Otherwise, there is no answer.
"""
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(1)
def specialArray(nums: List[int]) -> int:
    for i in range(1, len(nums) + 1):
        cnt = 0
        for num in nums:
            if num >= i:
                cnt += 1
        if cnt == i:
            return i
    return -1


# Time complexity: O(n log n)
# Space complexity: O(1)
def specialArray1(nums: list[int]) -> int:
    l, r = 1, len(nums)
    while l <= r:
        mid = (l + r) >> 1
        cnt = sum(1 for num in nums if num >= mid)

        if cnt == mid:
            return mid

        if cnt < mid:
            r = mid - 1
        else:
            l = mid + 1

    return -1


assert specialArray([3, 5]) == 2
assert specialArray([0, 0]) == -1
assert specialArray([0, 4, 3, 0, 4]) == 3
