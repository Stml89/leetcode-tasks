"""
1331. Rank Transform of an Array

Given an array of integers arr, replace each element with its rank.
The rank represents how large the element is. The rank has the following rules:
- Rank is an integer starting from 1.
- The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
- Rank should be as small as possible.

Example 1:
Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.

Example 2:
Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.

Example 3:
Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]

Constraints:
0 <= arr.length <= 105
-109 <= arr[i] <= 109

Hint 1
Use a temporary array to copy the array and sort it.

Hint 2
The rank of each element is the number of unique elements smaller than it in the sorted array plus one.
"""
from typing import List


# Time complexity: O(n + k log k), where k is the number of unique elements
# Space complexity: O(n)
def arrayRankTransform(arr: List[int]) -> List[int]:
    sorted_unique = sorted(set(arr))
    rank_map = {value: index + 1 for index, value in enumerate(sorted_unique)}
    return [rank_map[num] for num in arr]


assert arrayRankTransform([40, 10, 20, 30]) == [4, 1, 2, 3]
assert arrayRankTransform([100, 100, 100]) == [1, 1, 1]
assert arrayRankTransform([37, 12, 28, 9, 100, 56, 80, 5, 12]) == [5, 3, 4, 2, 8, 6, 7, 1, 3]
