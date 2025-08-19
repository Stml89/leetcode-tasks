"""
766. Toeplitz Matrix

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.

Hint 1
Check whether each value is equal to the value of it's top-left neighbor.

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 20
0 <= matrix[i][j] <= 99

Follow up:
What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
What if the matrix is so large that you can only load up a partial row into the memory at once?
"""
# TODO example
from typing import List


def isToeplitzMatrix(matrix: List[List[int]]) -> bool:
    for x in range(len(matrix) - 1):
        for y in range(len(matrix[0]) - 1):
            if matrix[x][y] != matrix[x+1][y+1]:
                return False
    return True


assert isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
assert not isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 6]])
assert not isToeplitzMatrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 6, 1, 2]])
assert not isToeplitzMatrix([[1, 2], [2, 2]])
