"""
1812. Determine Color of a Chessboard Square

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard for your reference.
Return true if the square is white, and false if the square is black.
The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and the number second.

Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false

Constraints:
coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'

Hint 1
Convert the coordinates to (x, y) - that is, "a1" is (1, 1), "d7" is (4, 7).
Hint 2
Try add the numbers together and look for a pattern.
"""


# Time Complexity: O(1)
# Space Complexity: O(1)
def squareIsWhite(coordinates: str) -> bool:
    column = ord(coordinates[0]) - ord("a") + 1
    row = int(coordinates[1])

    return (column + row) % 2 == 1


assert squareIsWhite("a1") is False
assert squareIsWhite("h3") is True
assert squareIsWhite("c7") is False
