"""
1967. Number of Strings That Appear as Substrings in Word

Given an array of strings patterns and a string word, return the number of strings in patterns 
that exist as a substring in word.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

Example 2:
Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

Example 3:
Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".
 
Constraints:
1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
patterns[i] and word consist of lowercase English letters.

Hint 1
Deal with each of the patterns individually.

Hint 2
Use the built-in function in the language you are using to find if the pattern exists as a substring in word.
"""
from typing import List


# Time Complexity: O(p * w), where p - str count in pattern, w - len of word
# Space Complexity: O(1)
def numOfStrings(patterns: List[str], word: str) -> int:
    cnt = 0
    for i in patterns:
        if i in word:
            cnt += 1

    return cnt


# Time Complexity: O(p * w)
# Space Complexity: O(1)
def numOfStrings1(patterns: List[str], word: str) -> int:
    return sum(pattern in word for pattern in patterns)


# Time Complexity: O(p * w)
# Space Complexity: O(p)
def numOfStrings2(patterns: List[str], word: str) -> int:
    return len(list(filter(lambda p: p in word, patterns)))


assert numOfStrings(["a", "abc", "bc", "d"], "abc") == 3
assert numOfStrings(["a", "b", "c"], "aaaaabbbbb") == 2
assert numOfStrings(["a", "a", "a"], "ab") == 3
assert numOfStrings(["hello"], "hello world") == 1
assert numOfStrings(["x", "y", "z"], "abcdef") == 0
assert numOfStrings(["ab", "bc", "cd"], "abcd") == 3
assert numOfStrings(["aa", "aaa", "aaaa"], "aaaa") == 3
