"""
1909. Remove One Element to Make the Array Strictly Increasing

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly 
one element, or false otherwise. If the array is already strictly increasing, return true.
The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).


Example 1:
Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.

Example 2:
Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.

Example 3:
Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
 
Constraints:
2 <= nums.length <= 1000
1 <= nums[i] <= 1000

Hint 1
For each index i in nums remove this index.

Hint 2
If the array becomes sorted return true, otherwise revert to the original array and try different index.
"""
from typing import List


# Time Complexity: O(n^2)
# Space Complexity: O(n)
def canBeIncreasing(nums: List[int]):
    for i in range(len(nums)):
        arr = nums[:i] + nums[i + 1:]

        if all(arr[j - 1] < arr[j] for j in range(1, len(arr))):
            return True

    return False


assert canBeIncreasing([1, 2, 10, 5, 7]) is True
assert canBeIncreasing([2, 3, 1, 2]) is False
assert canBeIncreasing([1, 1, 1]) is False
assert canBeIncreasing([1, 2, 3, 4]) is True
assert canBeIncreasing([1, 2, 3, 2]) is True
assert canBeIncreasing([1, 2, 2, 3]) is True
assert canBeIncreasing([1, 2, 3, 1]) is True
assert canBeIncreasing([3, 4, 2, 3]) is False

