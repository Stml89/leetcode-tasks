"""
1232. Check If It Is a Straight Line

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Explanation: The points form a straight line.

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
Explanation: The points do not form a straight line.

Constraints:
2 <= coordinates.length <= 1000
3 <= coordinates[i].length <= 10
-10000 <= coordinates[i][0], coordinates[i][1] <= 10000

Hint 1
To check if all points lie on the same straight line, we can calculate the slope between the first two
points and then verify that the slope between the first point and each subsequent point is the same.

Hint 2
We can avoid division when calculating slopes to prevent division by zero errors. Instead of comparing
slopes directly, we can cross-multiply to compare the products.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def checkStraightLine(coordinates: List[List[int]]) -> bool:
    if len(coordinates) <= 2:
        return True

    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    dx = x1 - x0
    dy = y1 - y0

    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if dy * (x - x0) != dx * (y - y0):
            return False
    return True


# Time complexity: O(n)
# Space complexity: O(1)
def checkStraightLine1(coordinates: List[List[int]]) -> bool:
    (x0, y0), (x1, y1) = coordinates[0], coordinates[1]
    for x, y in coordinates[2:]:
        if (y1 - y0) * (x - x1) != (y - y1) * (x1 - x0):
            return False
    return True


assert checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
assert not checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
assert checkStraightLine([[0, 0], [0, 1], [0, -1]])
