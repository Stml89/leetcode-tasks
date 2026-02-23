"""
1337. The K Weakest Rows in a Matrix

You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians).
The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of
all the 0's in each row.

A row i is weaker than a row j if one of the following is true:
- The number of soldiers in row i is less than the number of soldiers in row j.
- Both rows have the same number of soldiers and i < j.

Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Example 1:
Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers in each row is:
- Row 0: 2
- Row 1: 4
- Row 2: 1
- Row 3: 2
- Row 4: 5
The rows ordered from weakest to strongest are [2,0,3,1,4].

Example 2:
Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers in each row is:
- Row 0: 1
- Row 1: 4
- Row 2: 1
- Row 3: 1
The rows ordered from weakest to strongest are [0,2,3,1].

Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.

Hint 1
Sort the matrix row indexes by the number of soldiers and then row indexes.
"""
from collections import defaultdict
from typing import List


# Time complexity: O(n * m)
# Space complexity: O(n)
def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    soldiers = defaultdict(list)

    for i in range(len(mat)):
        count = sum(mat[i])
        soldiers[count].append(i)

    result = []
    for key in sorted(soldiers.keys()):
        for index in soldiers[key]:
            if len(result) < k:
                result.append(index)
            else:
                return result

    return result


# Time complexity: O(n * m + n log n)
# Space complexity: O(n)
def kWeakestRows(mat: List[List[int]], k: int) -> List[int]:
    candidates = []
    for i, row in enumerate(mat):
        candidates.append([sum(row), i])
    candidates.sort(key=lambda c: (c[0], c[1]))
    return [i for _, i in candidates[:k]]


assert kWeakestRows([[1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 0],
                     [1, 0, 0, 0, 0],
                     [1, 1, 0, 0, 0],
                     [1, 1, 1, 1, 1]], 3) == [2, 0, 3]
assert kWeakestRows([[1, 0, 0, 0],
                     [1, 1, 1, 1],
                     [1, 0, 0, 0],
                     [1, 0, 0, 0]], 2) == [0, 2]
