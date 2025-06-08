"""
566. Reshape the Matrix
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with
 a different size r x c keeping its original data.
You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.
The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.
If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
  1 2   -> 1, 2, 3, 4
  3 4
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:
  1 2   -> 1, 2
  3 4      3, 4
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if not mat:
        return mat
    if len(mat) * len(mat[0]) != r * c:
        return mat

    reshaped_arr = []
    mat2 = [i for arr in mat for i in arr]

    rows = int(len(mat2) / r)
    count = 0
    for i in range(0, len(mat2), rows):
        reshaped_arr.extend([mat2[count:count + c]])
        count += c
    return reshaped_arr
    # l = []
    # res = []
    # m = len(mat)
    # n = len(mat[0])
    # for i in range(m):
    #     for j in range(n):
    #         l.append(mat[i][j])
    # if len(l) != r * c:
    #     return mat
    # j = 0
    # for i in range(r):
    #     res.append(l[j:j + c])
    #     j = j + c
    # return res


assert matrixReshape([[1, 2], [3, 4]], r=1, c=4) == [[1, 2, 3, 4]]
assert matrixReshape([[1, 2], [3, 4]], r=2, c=4) == [[1, 2], [3, 4]]
assert matrixReshape([[1, 2], [3, 4], [5, 6]], r=2, c=3) == [[1, 2, 3], [4, 5, 6]]
assert matrixReshape([[1, 2], [3, 4]], r=4, c=1) == [[1], [2], [3], [4]]
assert matrixReshape([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]], r=42, c=5) == [
    [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
