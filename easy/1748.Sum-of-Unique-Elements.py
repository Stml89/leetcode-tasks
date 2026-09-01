"""
1748. Sum of Unique Elements

You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.
Return the sum of all the unique elements of nums.

Example 1:
Input: nums = [1,2,3,2]
Output: 4
Explanation: The unique elements are [1,3], and the sum is 4.

Example 2:
Input: nums = [1,1,1,1,1]
Output: 0
Explanation: There are no unique elements, and the sum is 0.

Example 3:
Input: nums = [1,2,3,4,5]
Output: 15
Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.

Constraints:
1 <= nums.length <= 100
1 <= nums[i] <= 100

Hint 1
Use a dictionary to count the frequency of each number.
"""
from collections import Counter
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def sumOfUnique(nums: List[int]) -> int:
    count = Counter(nums)
    return sum(num for num, freq in count.items() if freq == 1)


assert sumOfUnique([1, 2, 3, 4, 5]) == 15
assert sumOfUnique([1, 1, 1, 1, 1]) == 0
assert sumOfUnique([1, 2, 3, 2]) == 4
