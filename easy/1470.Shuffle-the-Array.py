"""
1470. Shuffle the Array

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
1 <= n <= 500
nums.length == 2n
1 <= nums[i] <= 10^3

Hint 1
Use two pointers to create the new array of 2n elements. The first starting at the beginning and the other
starting at (n+1)th position. Alternate between them and create the new array.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def shuffle(nums: List[int], n: int) -> List[int]:
    p_first = 0
    p_second = n
    result = []
    for i in range(n):
        result.append(nums[p_first])
        p_first += 1
        result.append(nums[p_second])
        p_second += 1
    return result


# Time complexity: O(n)
# Space complexity: O(n)
def shuffle1(nums: List[int], n: int) -> List[int]:
    result = [0] * (2 * n)
    for i in range(n):
        result[2 * i] = nums[i]
        result[2 * i + 1] = nums[i + n]
    return result


assert shuffle([2, 5, 1, 3, 4, 7], 3) == [2, 3, 5, 4, 1, 7]
assert shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4) == [1, 4, 2, 3, 3, 2, 4, 1]
assert shuffle([1, 1, 2, 2], 2) == [1, 2, 1, 2]
