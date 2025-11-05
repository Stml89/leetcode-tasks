"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
- The town judge trusts nobody.
- Everybody (except for the town judge) trusts the town judge.
- There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person
labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
Input: n = 2, trust = [[1,2]]
Output: 2

Example 2:
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3

Example 3:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1

Constraints:
1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def findJudge(n: int, trust: List[List[int]]) -> int:
    res = [0] * n
    for a, b in trust:
        res[a - 1] -= 1
        res[b - 1] += 1

    for i in range(n):
        if res[i] == n - 1:
            return i + 1
    return -1


assert findJudge(n=2, trust=[[1, 2]]) == 2
assert findJudge(n=3, trust=[[1, 3], [2, 3]]) == 3
assert findJudge(n=3, trust=[[1, 3], [2, 3], [3, 1]]) == -1
assert findJudge(n=4, trust=[[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
assert findJudge(1, []) == 1
assert findJudge(2, []) == -1
