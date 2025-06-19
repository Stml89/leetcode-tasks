"""
645. Set Mismatch
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately,
due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition
of one number and loss of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Example 2:
Input: nums = [1,1]
Output: [1,2]

Constraints:
2 <= nums.length <= 104
1 <= nums[i] <= 104
"""
from collections import Counter
from typing import List


def findErrorNums(nums: List[int]) -> List[int]:
    # m_num = 0
    # d_num = 0
    # c = Counter(nums)
    #
    # for i in range(1, len(nums) + 1):
    #     if c[i] == 0:
    #         m_num = i
    #     if c[i] == 2:
    #         d_num = i
    # return [d_num, m_num]
    # ================================
    total = sum(range(1, len(nums) + 1))
    actual = sum(nums)
    unique = sum(set(nums))

    duplicate = actual - unique
    missing = total - unique

    return [duplicate, missing]


assert findErrorNums([1, 2, 2, 4]) == [2, 3]
assert findErrorNums([1, 1]) == [1, 2]
assert findErrorNums([2, 2]) == [2, 1]
assert findErrorNums([3, 2, 2]) == [2, 1]
assert findErrorNums([3, 2, 3, 4, 6, 5]) == [3, 1]
