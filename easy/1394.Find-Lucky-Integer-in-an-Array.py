"""
1394. Find Lucky Integer in an Array

Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
Return the largest lucky integer in the array. If there is no lucky integer return -1.

Example 1:
Input: arr = [2,2,3,4]
Output: 2
Explanation: The only lucky number in the array is 2 because frequency[2] == 2.

Example 2:
Input: arr = [1,2,2,3,3,3]
Output: 3
Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.

Example 3:
Input: arr = [2,2,2,3,3]
Output: -1
Explanation: There are no lucky numbers in the array.

Constraints:
1 <= arr.length <= 500
1 <= arr[i] <= 500

Hint 1
Count the frequency of each integer in the array.

Hint 2
Get all lucky numbers and return the largest of them.
"""
from collections import Counter
from typing import List


# Time complexity: O(m)
# Space complexity: O(n)
def findLucky(arr: List[int]) -> int:
    d = {}
    for number in arr:
        d[number] = d.get(number, 0) + 1

    lucky_numbers = [num for num, freq in d.items() if num == freq]
    return max(lucky_numbers) if lucky_numbers else -1


assert findLucky([2, 2, 3, 4]) == 2
assert findLucky([1, 2, 2, 3, 3, 3]) == 3
assert findLucky([2, 2, 2, 3, 3]) == -1
