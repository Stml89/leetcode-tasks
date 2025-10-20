"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.
Recall that arr is a mountain array if and only if:
- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
-- arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
-- arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 104

Hint 1
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be
able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no
mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with
a straightforward solution.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def validMountainArray(arr: List[int]) -> bool:
    is_decreasing = False
    is_increasing = False
    if len(arr) < 3:
        return False

    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > prev:
            if is_decreasing:
                return False
            is_increasing = True
            prev = arr[i]
        elif prev > arr[i]:
            is_decreasing = True
            prev = arr[i]
        else:
            return False

    return is_decreasing and is_increasing


# Time complexity: O(n)
# Space complexity: O(1)
def validMountainArray1(arr: List[int]) -> bool:
    left, right = 1, len(arr) - 2

    if left > right:
        return False  # length < 3
    if arr[left] <= arr[left - 1]:
        return False
    if arr[right] <= arr[right + 1]:
        return False

    while left < right and arr[left] < arr[left + 1]:
        left += 1
    while left <= right and arr[right] < arr[right - 1]:
        right -= 1

    return left >= right


assert not validMountainArray([2, 1])
assert not validMountainArray([3, 5, 5])
assert not validMountainArray([1, 2, 3, 2, 3])
assert not validMountainArray([3, 5, 7])
assert not validMountainArray([10, 5, 2])
assert validMountainArray([0, 3, 2, 1])
