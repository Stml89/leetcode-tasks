"""
696. Count Binary Substrings
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
and all the 0's and all the 1's in these substrings are grouped consecutively.
Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Constraints:
1 <= s.length <= 105
s[i] is either '0' or '1'.

Hint 1
How many valid binary substrings exist in "000111", and how many in "11100"? What about "00011100"?
"""
def countBinarySubstrings(s: str) -> int:
    groups = []
    cnt = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            groups.append(cnt)
            cnt = 1
    groups.append(cnt)

    ans = 0
    for i in range(len(groups) - 1):
        ans += min(groups[i], groups[i + 1])

    return ans


assert countBinarySubstrings("00110011") == 6
assert countBinarySubstrings("10101") == 4
