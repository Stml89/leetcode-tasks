"""
1252. Cells with Odd Values in a Matrix

There is an m x n matrix that is initialized to all 0's. There is also a 2D array indices where each indices[i] =
[ri, ci] represents a 0-indexed location to perform some increment operations on the matrix.

For each location indices[i], do both of the following:
- Increment all the cells on row ri.
- Increment all the cells on column ci.

Given m, n, and indices, return the number of odd-valued cells in the matrix after applying the
increment to all locations in indices.

Example 1:
| 0 0 0 | -> | 1 2 1 | -> | 1 3 1 |
| 0 0 0 | -> | 0 1 0 | -> | 1 3 1 |
Input: m = 2, n = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix is [[1,3,1],[1,3,1]], which contains 6 odd numbers.

Example 2:
| 0 0 | -> | 0 1 | -> | 2 2 |
| 0 0 | -> | 1 2 | -> | 2 2 |
Input: m = 2, n = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There are no odd numbers in the final matrix.

Constraints:
1 <= m, n <= 50
1 <= indices.length <= 100
0 <= ri < m
0 <= ci < n

Follow up: Could you solve this in O(n + m + indices.length) time with only O(n + m) extra space?

Hint 1
Simulation : With small constraints, it is possible to apply changes to each row and column and count odd cells after applying it.

Hint 2
You can accumulate the number you should add to each row and column and then you can count the number of odd cells.
"""
from typing import List


# Time complexity: O(m * n + k * (m + n)) where k is the length of indices
# Space complexity: O(m + n)
def oddCells(m: int, n: int, indices: List[List[int]]) -> int:
    matrix = [[0] * n for _ in range(m)]

    for r, c in indices:
        for row in range(m):
            matrix[row][c] += 1
        for col in range(n):
            matrix[r][col] += 1

    odd_count = 0
    for row in range(m):
        for col in range(n):
            if matrix[row][col] % 2 != 0:
                odd_count += 1

    return odd_count


assert oddCells(2, 3, [[0, 1], [1, 1]]) == 6
assert oddCells(2, 2, [[1, 1], [0, 0]]) == 0
