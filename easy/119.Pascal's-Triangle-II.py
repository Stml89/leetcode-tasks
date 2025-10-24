"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
"""
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(n)
def getRow(rowIndex: int) -> List[int]:
    row = []
    result = []
    for _ in range(rowIndex + 1):
        row = [1] + row
        for i in range(1, len(row) - 1):
            row[i] += row[i + 1]
        result.append(row)

    return result[-1]


assert getRow(3) == [1, 3, 3, 1]
assert getRow(0) == [1]
assert getRow(1) == [1, 1]
