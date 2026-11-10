"""
1929. Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] 
and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.

Example 1:
Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Example 2:
Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]
 
Constraints:
n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 1000

Hint 1
Build an array of size 2 * n and assign nums[i] to ans[i] and ans[i + n]
"""
from typing import List


# Time Complexity: O(n)
# Space Complexity: O(n)
def getConcatenation(nums: List[int]) -> List[int]:
    return nums + nums


# Time Complexity: O(n)
# Space Complexity: O(n)
def getConcatenation1(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]

    return ans


assert getConcatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert getConcatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
assert getConcatenation([5]) == [5, 5]
assert getConcatenation([7, 8]) == [7, 8, 7, 8]
