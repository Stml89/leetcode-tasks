"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def repeatedSubstringPattern(s: str) -> bool:
    s2 = s + s
    s2 = s2[1:len(s2) - 1]
    if s in s2:
        return True
    return False


assert repeatedSubstringPattern("abab")
assert not repeatedSubstringPattern("aba")
assert repeatedSubstringPattern("abcabcabcabc")
assert not repeatedSubstringPattern("ababba")
assert repeatedSubstringPattern("abaababaab")
