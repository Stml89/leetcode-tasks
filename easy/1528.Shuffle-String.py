"""
1528. Shuffle String

You are given a string s and an integer array indices of the same length.
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
Return the shuffled string.

Example 1:
"codeleet"
 ||||||||
 45670213
"leetcode"
Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
Output: "leetcode"
Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

Example 2:
Input: s = "abc", indices = [0,1,2]
Output: "abc"
Explanation: After shuffling, each character remains in its position.

Constraints:
s.length == indices.length == n
1 <= n <= 100
s consists of only lowercase English letters.
0 <= indices[i] < n
All values of indices are unique.

Hint 1
You can create an auxiliary string t of length n.

Hint 2
Assign t[indexes[i]] to s[i] for each i from 0 to n-1.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def restoreString(s: str, indices: List[int]) -> str:
    result = [''] * len(s)
    for i in range(len(s)):
        result[indices[i]] = s[i]
    return ''.join(result)


assert restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]) == "leetcode"
assert restoreString("abc", [0, 1, 2]) == "abc"
