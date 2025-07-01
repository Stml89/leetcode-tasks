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
def validPalindrome(s: str) -> bool:
    # O(n)
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start] != s[end]:
            skip_start = s[start + 1: end + 1]
            skip_end = s[start:end]
            return skip_start == skip_start[::-1] or skip_end == skip_end[::-1]
        start += 1
        end -= 1

    return True

    # O(n2)
    # if s == s[::-1]:
    #     return True
    # curr = 0
    # while curr < len(s):
    #     tmp = s[:curr] + s[curr + 1:]
    #     print(tmp)
    #     if tmp == tmp[::-1]:
    #         return True
    #     curr += 1
    # return False


assert validPalindrome("aba")
assert validPalindrome("abca")
assert not validPalindrome("abc")
assert validPalindrome("eccer")
