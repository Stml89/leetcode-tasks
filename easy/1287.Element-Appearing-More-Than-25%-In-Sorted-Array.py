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


assert findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]) == 6
assert findSpecialInteger([1, 1]) == 1
