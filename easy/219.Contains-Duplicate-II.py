"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array
such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    r = {}
    for indx, value in enumerate(nums):
        if value in r.keys() and abs(r[value] - indx) <= k:
            return True
        else:
            r[value] = indx

    return False


# Time complexity: O(n)
# Space complexity: O(n)
def containsNearbyDuplicate1(nums: List[int], k: int) -> bool:
    r = set()
    for indx, value in enumerate(nums):
        if value in r:
            return True
        else:
            r.add(value)

        if len(r) > k:
            r.remove(nums[indx - k])

    return False


assert containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3)
assert containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
assert not containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2)
