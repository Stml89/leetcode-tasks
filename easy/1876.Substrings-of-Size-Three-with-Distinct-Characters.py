"""
1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.
Given a string 's', return the number of good substrings of length three in 's'.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

Example 1:
Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz".
The only good substring of length 3 is "xyz".
Example 2:
Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".

Constraints:
1 <= s.length <= 100
's' consists of lowercase English letters.

Hint 1
Try using a set to find out the number of distinct characters in a substring.
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def countGoodSubstrings(s: str) -> int:
    result = 0

    for i in range(len(s) - 2):
        if len(set(s[i:i + 3])) == 3:
            result += 1

    return result


# Time Complexity: O(n)
# Space Complexity: O(1)
def countGoodSubstrings1(s: str) -> int:
    result = 0

    for i in range(len(s) - 2):
        a, b, c = s[i], s[i + 1], s[i + 2]

        if a != b and b != c and a != c:
            result += 1

    return result


# Time Complexity: O(n)
# Space Complexity: O(1)
def countGoodSubstrings2(s: str) -> int:
    return sum(
        len({a, b, c}) == 3
        for a, b, c in zip(s, s[1:], s[2:])
    )


assert countGoodSubstrings("xyzzaz") == 1
assert countGoodSubstrings("aababcabc") == 4
assert countGoodSubstrings("abc") == 1
assert countGoodSubstrings("aaa") == 0
assert countGoodSubstrings("abcdef") == 4
assert countGoodSubstrings("abca") == 2
assert countGoodSubstrings("a") == 0
assert countGoodSubstrings("ab") == 0
