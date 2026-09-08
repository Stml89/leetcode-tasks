"""
1763. Longest Nice Substring

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase.
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b'
appears, but 'B' does not.
Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the
earliest occurrence. If there are none, return an empty string.

Example 1:
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.

Example 2:
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.

Example 3:
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.

Constraints:
1 <= s.length <= 100
s consists of uppercase and lowercase English letters.

Hint 1
Brute force and check each substring to see if it is nice.
"""


# Time complexity: O(n^3)
# Space complexity: O(n)
def longestNiceSubstring(s: str) -> str:
    def is_nice(substring: str) -> bool:
        char_set = set(substring)
        for char in char_set:
            if char.islower() and char.upper() not in char_set:
                return False
            if char.isupper() and char.lower() not in char_set:
                return False
        return True

    longest_nice = ""
    n = len(s)

    for i in range(n):
        for j in range(i + 1, n + 1):
            substring = s[i:j]
            if is_nice(substring) and len(substring) > len(longest_nice):
                longest_nice = substring

    return longest_nice


# Time complexity: O(n^2)
# Space complexity: O(n)
def longestNiceSubstring1(s: str) -> str:
    if len(s) < 2:
        return ""

    chars = set(s)

    for i, ch in enumerate(s):
        if ch.swapcase() not in chars:
            left = longestNiceSubstring1(s[:i])
            right = longestNiceSubstring1(s[i + 1:])

            return left if len(left) >= len(right) else right

    return s


assert longestNiceSubstring("YazaAay") == "aAa"
assert longestNiceSubstring("Bb") == "Bb"
assert longestNiceSubstring("c") == ""
