"""
661. Image Smoother
An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by rounding
down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the
average of the four cells in the red smoother).
     __ __ __
    |01 02 03| 04 05
    |06 07 08| 09 10
    |11 12 13| 14 15
    |-- -- -- -- -- --|
     16 17 18 |19 20  |
     21 22 23 |24 25  |
              |_______|
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.

Example 1:
  1 1 1    =>   0 0 0
  1 0 1    =>   0 0 0
  1 1 1    =>   0 0 0
Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Example 2:
  100 200 100   =>   137 141 137
  200  5  200   =>   141 138 141
  100 200 100   =>   137 141 137
Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

Constraints:
m == img.length
n == img[i].length
1 <= m, n <= 200
0 <= img[i][j] <= 255
"""
# TODO
from typing import List


def imageSmoother(img: List[List[int]]) -> List[List[int]]:
    m, n = len(img), len(img[0])
    output = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            ans = cnt = 0
            for m_row in range(i - 1, i + 2):
                for n_col in range(j - 1, j + 2):
                    if 0 <= m_row < m and 0 <= n_col < n:
                        cnt += 1
                        ans += img[m_row][n_col]

            output[i][j] = ans // cnt

    return output


assert imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
assert imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [[137, 141, 137], [141, 138, 141],
                                                                             [137, 141, 137]]
