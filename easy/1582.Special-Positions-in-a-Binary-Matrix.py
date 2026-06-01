"""
1582. Special Positions in a Binary Matrix

Given an m x n binary matrix mat, return the number of special positions in mat.
A position (i, j) is called special if mat[i][j] == 1 and all other elements in row i and column j are
0 (rows and columns are 0-indexed).

Example 1:
 1 0 0
 0 0 1
 1 0 0
Input: mat = [[1,0,0],[0,0,1],[1,0,0]]
Output: 1
Explanation: (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
1 0 0
0 1 0
0 0 1
Input: mat = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
Explanation: (0, 0), (1, 1) and (2, 2) are special positions.

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
mat[i][j] is either 0 or 1.

Hint 1
Keep track of 1s in each row and in each column. Then while iterating over matrix, if the current position
is 1 and current row as well as current column contains exactly one occurrence of 1.
"""
from typing import List


# Time complexity: O(m * n)
# Space complexity: O(m + n)
def numSpecial(mat: List[List[int]]) -> int:
    row = [0] * len(mat)
    col = [0] * len(mat[0])

    for i in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[i][y] == 1:
                row[i] += 1
                col[y] += 1

    count = 0
    for i in range(len(mat)):
        for y in range(len(mat[0])):
            if mat[i][y] == 1 and row[i] == 1 and col[y] == 1:
                count += 1
    return count


assert numSpecial([[1, 0, 0], [0, 0, 1], [1, 0, 0]]) == 1
assert numSpecial([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
