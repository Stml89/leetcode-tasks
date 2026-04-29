"""
1502. Can Make Arithmetic Progression From Sequence

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.

Constraints:
2 <= arr.length <= 1000
-106 <= arr[i] <= 106

Hint 1
Consider that any valid arithmetic progression will be in sorted order.

Hint 2
Sort the array, then check if the differences of all consecutive elements are equal.
"""
from typing import List


# Time complexity: O(n log n)
# Space complexity: O(1)
def canMakeArithmeticProgression(arr: List[int]) -> bool:
    arr.sort()
    common_diff = arr[1] - arr[0]

    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != common_diff:
            return False

    return True


assert canMakeArithmeticProgression([3, 5, 1]) == True
assert canMakeArithmeticProgression([1, 2, 4]) == False
