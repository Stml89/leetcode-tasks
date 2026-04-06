"""
1437. Check If All 1's Are at Least Length K Places Away

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

Example 1:
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.

Example 2:
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.


Constraints:
1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1

Hint 1
Each time you find a number 1, check whether or not it is K or more places away from the next one. If it's not, return false.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def kLengthApart(nums: List[int], k: int) -> bool:
    for i in range(len(nums)):
        if nums[i] == 1:
            for j in range(i + 1, min(i + k + 1, len(nums))):
                if nums[j] == 1:
                    return False
    return True


# Time complexity: O(n)
# Space complexity: O(1)
def kLengthApart1(nums: List[int], k: int) -> bool:
    prev = -1

    for i, num in enumerate(nums):
        if num == 1:
            if prev != -1 and i - prev - 1 < k:
                return False
            prev = i

    return True


assert kLengthApart([1, 0, 0, 1, 0, 0, 1], 2) == True
assert kLengthApart([1, 0, 0, 1, 0, 1], 2) == False
assert kLengthApart([1, 1, 1, 1, 1], 0) == True
