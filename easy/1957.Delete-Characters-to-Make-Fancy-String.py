"""
1957. Delete Characters to Make Fancy String

A fancy string is a string where no three consecutive characters are equal.
Given a string s, delete the minimum possible number of characters from s to make it fancy.
Return the final string after the deletion. It can be shown that the answer will always be unique.

Example 1:
Input: s = "leeetcode"
Output: "leetcode"
Explanation:
Remove an 'e' from the first group of 'e's to create "leetcode".
No three consecutive characters are equal, so return "leetcode".

Example 2:
Input: s = "aaabaaaa"
Output: "aabaa"
Explanation:
Remove an 'a' from the first group of 'a's to create "aabaaaa".
Remove two 'a's from the second group of 'a's to create "aabaa".
No three consecutive characters are equal, so return "aabaa".

Example 3:
Input: s = "aab"
Output: "aab"
Explanation: No three consecutive characters are equal, so return "aab".
 
Constraints:
1 <= s.length <= 105
s consists only of lowercase English letters.

Hint 1
What's the optimal way to delete characters if three or more consecutive characters are equal?

Hint 2
If three or more consecutive characters are equal, keep two of them and delete the rest.
"""
from itertools import groupby


# Time Complexity: O(n)
# Space Complexity: O(n)
def makeFancyString(s: str) -> str:
    result = []

    for char in s:
        if len(result) < 2 or not (
            result[-1] == char and result[-2] == char
        ):
            result.append(char)

    return ''.join(result)


# Time Complexity: O(n)
# Space Complexity: O(n)
def makeFancyString1(s: str) -> str:
    result = []
    count = 0
    prev = None

    for char in s:
        if char == prev:
            count += 1
        else:
            count = 1
            prev = char

        if count <= 2:
            result.append(char)

    return ''.join(result)


assert makeFancyString("leeetcode") == "leetcode"
assert makeFancyString("aaabaaaa") == "aabaa"
assert makeFancyString("aab") == "aab"
assert makeFancyString("aaaaa") == "aa"
assert makeFancyString("aabbcc") == "aabbcc"
assert makeFancyString("abcabc") == "abcabc"
assert makeFancyString("aaaabbbbcccc") == "aabbcc"
assert makeFancyString("a") == "a"
assert makeFancyString("aabbbaa") == "aabbaa"
