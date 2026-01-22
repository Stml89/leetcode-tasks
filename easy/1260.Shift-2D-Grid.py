"""
1260. Shift 2D Grid

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:
- Element at grid[i][j] moves to grid[i][j + 1].
- Element at grid[i][n - 1] moves to grid[i + 1][0].
- Element at grid[m - 1][n - 1] moves to grid[0][0].

Return the 2D grid after applying shift operation k times.

Example 1:
|1,2,3|    |9,1,2|
|4,5,6| -> |3,4,5|
|7,8,9|    |6,7,8|
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:
|3,8,1,9]|     |12,0,21,13|
|19,7,2,5]| -> |3,8,1,9   |
|4,6,11,10]|   |19,7,2,5  |
|12,0,21,13]|  |4,6,11,10 |
Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:
|1,2,3|    |1,2,3|
|4,5,6| -> |4,5,6|
|7,8,9|    |7,8,9|
Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100

Hint 1
Simulate step by step. move grid[i][j] to grid[i][j+1]. handle last column of the grid.
Hint 2
Put the matrix row by row to a vector. take k % vector.length and move last k of the vector to the beginning.
put the vector to the matrix back the same way.
"""
from typing import List


# Time complexity: O(m * n)
# Space complexity: O(m * n)
def shiftGrid(grid: List[List[int]], k: int) -> List[List[int]]:
    m, n = len(grid), len(grid[0])
    if m == 0 or n == 0:
        return grid
    if k <= 0 or k % (m * n) == 0:
        return grid

    flat_list = [grid[i][j] for i in range(m) for j in range(n)]
    shifted_list = flat_list[-k:] + flat_list[:-k]

    i = 0
    for row in range(m):
        for col in range(n):
            grid[row][col] = shifted_list[i]
            i += 1

    return grid


assert shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
assert shiftGrid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4) == [[12, 0, 21, 13], [3, 8, 1, 9],
                                                                                        [19, 7, 2, 5], [4, 6, 11, 10]]
assert shiftGrid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
