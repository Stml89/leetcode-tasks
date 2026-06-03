"""
1588. Sum of All Odd Length Subarrays

Given an array of positive integers arr, return the sum of all possible odd-length subarrays of arr.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58

Example 2:
Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.

Example 3:
Input: arr = [10,11,12]
Output: 66

Constraints:
1 <= arr.length <= 100
1 <= arr[i] <= 1000

Follow up:
Could you solve this problem in O(n) time complexity?

Hint 1
You can brute force – try every (i,j) pair, and if the length is odd, go through and add the sum to the answer.
"""
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(1)
def sumOddLengthSubarrays1(arr: List[int]) -> int:
    count = 0
    for i in range(len(arr)):
        for y in range(i, len(arr)):
            if (y - i) % 2 == 0:
                count += sum(arr[i:y + 1])
    return count


# Time complexity: O(n)
# Space complexity: O(1)
def sumOddLengthSubarrays(arr: List[int]) -> int:
    count = 0
    for i in range(len(arr)):
        left = i + 1
        right = len(arr) - i
        count += arr[i] * ((left * right + 1) // 2)
    return count


assert sumOddLengthSubarrays([1, 4, 2, 5, 3]) == 58
assert sumOddLengthSubarrays([1, 2]) == 3
assert sumOddLengthSubarrays([10, 11, 12]) == 66
