"""
1886. Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target
by rotating mat in 90-degree increments, or false otherwise.

Example 1:
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.

Hint 1
What is the maximum number of rotations you have to check?

Hint 2
Is there a formula you can use to rotate a matrix 90 degrees?
"""


# Time Complexity: O(n²)
# Space Complexity: O(n²)
def findRotation(mat: list[list[int]], target: list[list[int]]) -> bool:
    for _ in range(4):
        if mat == target:
            return True

        mat = [list(row) for row in zip(*mat[::-1])]

    return False


# Time Complexity: O(n²)
# Space Complexity: O(n²)
def findRotation1(mat: list[list[int]], target: list[list[int]]) -> bool:
    def rotate(matrix: list[list[int]]) -> list[list[int]]:
        n = len(matrix)

        return [
            [matrix[n - 1 - j][i] for j in range(n)]
            for i in range(n)
        ]

    for _ in range(4):
        if mat == target:
            return True

        mat = rotate(mat)

    return False


# Time Complexity: O(n²)
# Space Complexity: O(1)
def findRotation2(mat: list[list[int]], target: list[list[int]]) -> bool:
    n = len(mat)

    for rotation in range(4):
        is_equal = True

        for i in range(n):
            for j in range(n):
                if rotation == 0:
                    x, y = i, j
                elif rotation == 1:
                    x, y = n - 1 - j, i
                elif rotation == 2:
                    x, y = n - 1 - i, n - 1 - j
                else:
                    x, y = j, n - 1 - i

                if mat[x][y] != target[i][j]:
                    is_equal = False
                    break

            if not is_equal:
                break

        if is_equal:
            return True

    return False


assert findRotation([[0, 1], [1, 0]], [[1, 0], [0, 1]]) is True
assert findRotation([[0, 1], [1, 1]], [[1, 0], [0, 1]]) is False
assert findRotation([[0, 0, 0], [0, 1, 0], [1, 1, 1]], [[1, 1, 1], [0, 1, 0], [0, 0, 0]]) is True
assert findRotation([[1]], [[1]]) is True
assert findRotation([[0]], [[1]]) is False
assert findRotation([[1, 0], [0, 1]], [[1, 0], [0, 1]]) is True
