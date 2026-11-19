"""
1961. Check If String Is a Prefix of Array

Given a string s and an array of strings words, determine whether s is a prefix string of words.
A string s is a prefix string of words if s can be made by concatenating the first k strings in 
words for some positive k no larger than words.length.
Return true if s is a prefix string of words, or false otherwise.

Example 1:
Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.

Example 2:
Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.

Hint 1
There are only words.length prefix strings.

Hint 2
Create all of them and see if s is one of them.
"""
from typing import List


# Time Complexity: O(n * m)
# Space Complexity: O(m)
def isPrefixString(s: str, words: List[str]) -> bool:
    prefix = ""

    for word in words:
        prefix += word

        if prefix == s:
            return True

        if len(prefix) >= len(s):
            return False

    return False


# Time Complexity: O(n * m)
# Space Complexity: O(m)
def isPrefixString1(s: str, words: List[str]) -> bool:
    prefix = []

    for word in words:
        prefix.append(word)
        current = ''.join(prefix)

        if current == s:
            return True

        if len(current) >= len(s):
            return False

    return False


# Time Complexity: O(m)
# Space Complexity: O(1)
def isPrefixString2(s: str, words: List[str]) -> bool:
    pos = 0

    for word in words:
        end = pos + len(word)

        if end > len(s) or s[pos:end] != word:
            return False

        pos = end

        if pos == len(s):
            return True

    return False


assert isPrefixString("a", ["a", "b"]) is True
assert isPrefixString("ab", ["a", "b", "c"]) is True
assert isPrefixString("abc", ["a", "b"]) is False
assert isPrefixString("abc", ["ab", "cd"]) is False
assert isPrefixString("hello", ["hello"]) is True
assert isPrefixString("hello", ["hell", "o"]) is True
