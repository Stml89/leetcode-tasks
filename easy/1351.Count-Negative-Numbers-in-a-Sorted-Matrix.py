"""
1351. Count Negative Numbers in a Sorted Matrix

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise,
return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],
               [3,2,1,-1],
               [1,1,-1,-2],
               [-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],
               [1,0]]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100

Follow up: Could you find an O(n + m) solution?

Hint 1
Use binary search for optimization or simply brute force.
"""
from typing import List


# Time complexity: O(m * n)
# Space complexity: O(1)
def countNegatives(grid: List[List[int]]) -> int:
    count = 0
    for row in grid:
        for col in row:
            if col < 0:
                count += 1
    return count


assert countNegatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]) == 8
assert countNegatives([[3, 2], [1, 0]]) == 0
