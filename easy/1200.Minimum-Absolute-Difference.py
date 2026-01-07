"""
1200. Minimum Absolute Difference

Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.
Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
- a, b are from arr
- a < b
- b - a equals to the minimum absolute difference of any two elements in arr

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]

Constraints:
2 <= arr.length <= 105
-106 <= arr[i] <= 106

Hint 1
Find the minimum absolute difference between two elements in the array.

Hint 2
The minimum absolute difference must be a difference between two consecutive elements in the sorted array.
"""
from typing import List


# Time complexity: O(n log n)
# Space complexity: O(n)
def minimumAbsDifference(arr: List[int]) -> List[List[int]]:
    s = sorted(arr)
    min_diff = float('inf')
    result = []
    for i in range(1, len(s)):
        diff = s[i] - s[i - 1]
        if diff < min_diff:
            result.clear()
            min_diff = diff
            result.append([s[i - 1], s[i]])
        elif diff == min_diff:
            result.append([s[i - 1], s[i]])

    return result


assert minimumAbsDifference([4, 2, 1, 3]) == [[1, 2], [2, 3], [3, 4]]
assert minimumAbsDifference([1, 3, 6, 10, 15]) == [[1, 3]]
assert minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]) == [[-14, -10], [19, 23], [23, 27]]
assert minimumAbsDifference([40, 11, 26, 27, -20]) == [[26, 27]]
