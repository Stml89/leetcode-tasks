"""
598. Range Addition II
You are given an m x n matrix M initialized with all 0's and an array of operations ops,
where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:
0 0 0      1 1 0      2 2 1
0 0 0      1 1 0      2 2 1
0 0 0      0 0 0      1 1 1
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.

Example 2:
Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4

Example 3:
Input: m = 3, n = 3, ops = []
Output: 9

Constraints:
1 <= m, n <= 4 * 104
0 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
"""
from typing import List


def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    # Работает, но не для всех примеров, тк вылетает по времени
    # lst = [0] * (m * n)
    # if not ops:
    #     return m * n
    #
    # for i in ops:
    #     for y in range(len(lst[:(i[0] * i[1])])):
    #         lst[y] += 1
    # return lst.count(max(lst))
    if not ops:
        return m * n

    for a, b in ops:
        m = min(m, a)
        n = min(n, b)
    return m * n


assert maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]) == 4
assert maxCount(m=3, n=3, ops=[[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3],
                               [3, 3]]) == 4
assert maxCount(m=3, n=3, ops=[]) == 9
assert maxCount(m=40000, n=40000, ops=[]) == 1600000000
assert maxCount(m=39999, n=39999, ops=[[19999, 19999]]) == 399960001
