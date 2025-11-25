"""
1037. Valid Boomerang

Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.
A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
Input: points = [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: points = [[1,1],[2,2],[3,3]]
Output: false

Constraints:
points.length == 3
points[i].length == 2
0 <= xi, yi <= 100

Hint 1
3 points form a boomerang if and only if the triangle formed from them has non-zero area.
"""
from typing import List


# Time complexity: O(1)
# Space complexity: O(1)
def isBoomerang(points: List[List[int]]) -> bool:
    x1, y1 = points[0]
    x2, y2 = points[1]
    x3, y3 = points[2]

    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    return area != 0


assert isBoomerang([[1, 1], [2, 3], [3, 2]])
assert not isBoomerang([[1, 1], [2, 2], [3, 3]])
