"""
1496. Path Crossing

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east,
or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location you
have previously visited. Return false otherwise.

Example 1:
         __
        | |
    (0, 0)
Input: path = "NES"
Output: false
Explanation: Notice that the path doesn't cross any point more than once.

Example 2:
       __
      | |
    ____
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

Constraints:
1 <= path.length <= 104
path[i] is either 'N', 'S', 'E', or 'W'.

Hint 1
Simulate the process while keeping track of visited points.
Hint 2
Use a set to store previously visited points.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def isPathCrossing(path: str) -> bool:
    visited = set()
    x, y = 0, 0
    visited.add((x, y))

    for direction in path:
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1

        if (x, y) in visited:
            return True
        visited.add((x, y))

    return False


assert isPathCrossing(path="NESW") == True
assert isPathCrossing(path="NES") == False
assert isPathCrossing(path="NESWW") == True
