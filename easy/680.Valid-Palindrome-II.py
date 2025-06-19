"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
1 <= s.length <= 105
s consists of lowercase English letters.
"""
# TODO
def validPalindrome(s: str) -> bool:
    if s == s[::-1]:
        return True
    curr = 0
    while curr < len(s) - 1:
        tmp = s[:curr] + s[curr + 1:]
        if tmp == tmp[::-1]:
            return True
        curr += 1
    return False


assert validPalindrome("aba")
assert validPalindrome("abca")
assert not validPalindrome("abc")
