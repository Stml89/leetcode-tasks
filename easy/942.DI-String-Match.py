"""
942. DI String Match

A permutation perm of n + 1 integers of all the integers in the range [0, n]
can be represented as a string s of length n where:
- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple
valid permutations perm, return any of them.

Example 1:
Input: s = "IDID"
Output: [0,4,1,3,2]

Example 2:
Input: s = "III"
Output: [0,1,2,3]

Example 3:
Input: s = "DDI"
Output: [3,2,0,1]

Constraints:
1 <= s.length <= 105
s[i] is either 'I' or 'D'.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def diStringMatch(s: str) -> List[int]:
    d = len(s)
    i = 0
    arr = []
    for item in range(len(s)):
        if s[item] == "I":
            arr.append(i)
            i += 1
        else:
            arr.append(d)
            d -= 1

    if s[-1] == 'I':
        arr.append(i)
    else:
        arr.append(d)

    return arr


# Time complexity: O(n)
# Space complexity: O(n)
def diStringMatch1(s: str) -> List[int]:
    low, high = 0, len(s)
    perm = []

    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        else:
            perm.append(high)
            high -= 1

    perm.append(low)
    return perm


assert diStringMatch("IDID") == [0, 4, 1, 3, 2]
assert diStringMatch("III") == [0, 1, 2, 3]
assert diStringMatch("DDI") == [3, 2, 0, 1]
