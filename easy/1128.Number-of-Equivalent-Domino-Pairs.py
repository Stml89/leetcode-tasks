"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only
if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1

Example 2:
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3

Constraints:
1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9

Hint 1
For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.

Hint 2
You can keep track of what you've seen using a hashmap.
"""
from collections import defaultdict
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def numEquivDominoPairs(dominoes: List[List[int]]) -> int:
    count_map = defaultdict(int)
    pair_count = 0

    for a, b in dominoes:
        key = (min(a, b), max(a, b))
        pair_count += count_map[key]
        count_map[key] += 1

    return pair_count


def numEquivDominoPairs1(dominoes: List[List[int]]) -> int:
    count = [0] * 100
    res = 0

    for a, b in dominoes:
        normalized = a * 10 + b if a < b else b * 10 + a
        res += count[normalized]
        count[normalized] += 1

    return res


assert numEquivDominoPairs([[1, 2], [2, 1], [3, 4], [5, 6]]) == 1
assert numEquivDominoPairs([[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]) == 3
