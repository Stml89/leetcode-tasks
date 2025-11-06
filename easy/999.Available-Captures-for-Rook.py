"""
999. Available Captures for Rook

You are given an 8 x 8 matrix representing a chessboard. There is exactly one white rook represented by 'R',
some number of white bishops 'B', and some number of black pawns 'p'. Empty squares are represented by '.'.
A rook can move any number of squares horizontally or vertically (up, down, left, right) until it reaches
another piece or the edge of the board. A rook is attacking a pawn if it can move to the pawn's square in one move.

Note: A rook cannot move through other pieces, such as bishops or pawns. This means a rook cannot attack a pawn if
there is another piece blocking the path.

Return the number of pawns the white rook is attacking.

Example 1:
Input: board = [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","R",".",".",".","p"],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 3
Explanation:
In this example, the rook is attacking all the pawns.

Example 2:
Input: board = [[".",".",".",".",".",".","."],
                [".","p","p","p","p","p",".","."],
                [".","p","p","B","p","p",".","."],
                [".","p","B","R","B","p",".","."],
                [".","p","p","B","p","p",".","."],
                [".","p","p","p","p","p",".","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 0
Explanation:
The bishops are blocking the rook from attacking any of the pawns.

Example 3:
Input: board = [[".",".",".",".",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                ["p","p",".","R",".","p","B","."],
                [".",".",".",".",".",".",".","."],
                [".",".",".","B",".",".",".","."],
                [".",".",".","p",".",".",".","."],
                [".",".",".",".",".",".",".","."]]

Output: 3
Explanation:
The rook is attacking the pawns at positions b5, d6, and f5.

Constraints:
board.length == 8
board[i].length == 8
board[i][j] is either 'R', '.', 'B', or 'p'
There is exactly one cell with board[i][j] == 'R'
"""
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(1)
def numRookCaptures(board: List[List[str]]) -> int:
    attack = 0
    pawn = 'p'
    bishop = 'B'
    x, y = -1, -1

    for i in range(len(board)):
        if "R" in board[i]:
            y = board[i].index("R")
            x, y = i, y
            break

    if x == -1 and y == -1:
        return -1

    if 0 < y <= len(board[x]):
        for i in range(len(board[x][:y - 1]), -1, -1):
            if bishop == board[x][i]:
                break
            if pawn == board[x][i]:
                attack += 1
                break

    for i in range(y + 1, len(board[x])):
        if bishop == board[x][i]:
            break
        if pawn == board[x][i]:
            attack += 1
            break

    if 0 < x <= len(board[i]):
        for i in range(x - 1, -1, -1):
            if bishop == board[i][y]:
                break
            if pawn == board[i][y]:
                attack += 1
                break

    for i in range(x + 1, len(board[x])):
        if bishop == board[i][y]:
            break
        if pawn == board[i][y]:
            attack += 1
            break

    return attack


board1 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "R", ".", ".", ".", "p"],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]
assert numRookCaptures(board1) == 3

board2 = [[".", ".", ".", ".", ".", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "B", "R", "B", "p", ".", "."],
          [".", "p", "p", "B", "p", "p", ".", "."],
          [".", "p", "p", "p", "p", "p", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]
assert numRookCaptures(board2) == 0

board3 = [[".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          ["p", "p", ".", "R", ".", "p", "B", "."],
          [".", ".", ".", ".", ".", ".", ".", "."],
          [".", ".", ".", "B", ".", ".", ".", "."],
          [".", ".", ".", "p", ".", ".", ".", "."],
          [".", ".", ".", ".", ".", ".", ".", "."]]
assert numRookCaptures(board3) == 3
