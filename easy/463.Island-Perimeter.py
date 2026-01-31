"""
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example 1:
Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:
Input: grid = [[1]]
Output: 4

Example 3:
Input: grid = [[1,0]]
Output: 4

Constraints:
row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.
There is exactly one island in grid.
"""
from typing import List


# Time complexity: O(m * n)
# Space complexity: O(1)
def islandPerimeter(grid: List[List[int]]) -> int:
    output = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                output += 4
                if i > 0 and grid[i - 1][j] == 1:
                    output -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    output -= 2
    return output


# Time complexity: O(m * n)
# Space complexity: O(1)
def islandPerimeter1(grid: List[List[int]]) -> int:
    column_length = len(grid)
    row_length = len(grid[0])
    count = 0
    for i in range(column_length):
        for j in range(row_length):
            if grid[i][j] == 1:
                if grid[i][j - 1] != 1 or j - 1 == -1:
                    count += 1
                if j + 1 == row_length:
                    count += 1
                elif grid[i][j + 1] != 1:
                    count += 1
                if grid[i - 1][j] != 1 or i - 1 == -1:
                    count += 1
                if i + 1 >= column_length:
                    count += 1
                elif grid[i + 1][j] != 1:
                    count += 1
    return count


assert islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]) == 16
assert islandPerimeter([[1]]) == 4
assert islandPerimeter([[1, 0]]) == 4
