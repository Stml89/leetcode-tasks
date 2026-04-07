"""
1446. Consecutive Characters

The power of the string is the maximum length of a non-empty substring that contains only one unique character.
Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters.

Hint 1
Keep an array power where power[i] is the maximum power of the i-th character.

Hint 2
The answer is max(power[i]).
"""


# Time complexity: O(n)
# Space complexity: O(1)
def maxPower(s: str) -> int:
    max_val = 0
    prev = ""
    count = 0
    for i in range(len(s)):
        if s[i] == prev:
            count += 1
        else:
            max_val = max(max_val, count)
            prev = s[i]
            count = 1
    return max(max_val, count)


# Time complexity: O(n)
# Space complexity: O(1)
def maxPower1(s: str) -> int:
    power = [0] * 26

    for i in range(len(s)):
        power[ord(s[i]) - ord('a')] = max(power[ord(s[i]) - ord('a')],
                                          1 + (power[ord(s[i - 1]) - ord('a')] if i > 0 and s[i] == s[i - 1] else 0))

    return max(power)


assert maxPower("leetcode") == 2
assert maxPower("abbcccddddeeeeedcba") == 5
