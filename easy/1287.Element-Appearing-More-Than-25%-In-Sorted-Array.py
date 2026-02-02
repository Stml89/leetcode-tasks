"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more
than 25% of the time, return that integer.

Example 1:
Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6

Example 2:
Input: arr = [1,1]
Output: 1

Constraints:
1 <= arr.length <= 104
0 <= arr[i] <= 105

Hint 1
Divide the array in four parts [1 - 25%] [25 - 50 %] [50 - 75 %] [75% - 100%]

Hint 2
The answer should be in one of the ends of the intervals.

Hint 3
In order to check which is element is the answer we can count the frequency with binarySearch.
"""
from collections import Counter
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def findSpecialInteger(arr: List[int]) -> int:
    d = Counter(arr)
    for k, v in d.items():
        if v > len(arr) // 4:
            return k


# Time complexity: O(n)
# Space complexity: O(1)
def findSpecialInteger1(arr: List[int]) -> int:
    threshold = len(arr) // 4
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
            if count > threshold:
                return arr[i]
        else:
            count = 1
    return arr[0]


# Time complexity: O(n)
# Space complexity: O(1)
def findSpecialInteger2(arr: List[int]) -> int:
    threshold = len(arr) // 4
    for i in range(len(arr) - threshold):
        if arr[i] == arr[i + threshold]:
            return arr[i]
    return arr[0]


assert findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
assert findSpecialInteger([1, 1]) == 1
