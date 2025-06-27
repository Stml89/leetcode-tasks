"""
697. Degree of an Array

Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: nums = [1,2,2,3,1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation:
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.

Constraints:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.

Hint 1
Say 5 is the only element that occurs the most number of times - for example, nums = [1, 5, 2, 3, 5, 4, 5, 6]. What is the answer?
"""
# TODO
from collections import Counter
from typing import List


def findShortestSubArray(nums: List[int]) -> int:
    c = Counter(nums)
    m = max(c.values())
    m_items = []
    for k, v in c.items():
        if v == m:
            m_items.append(k)

    minn = 1
    maxx = 0
    r = []
    for i in m_items:
        for idx, char in enumerate(nums):
            if char == i:
                minn = min(minn, idx)
                maxx = max(maxx, idx)
        r.append((maxx - minn) + 1)
        minn = 1
        maxx = 0
    return min(r)


assert findShortestSubArray([1, 2, 2, 3, 1]) == 2
assert findShortestSubArray([1, 2, 2, 3, 1, 4, 2]) == 6
