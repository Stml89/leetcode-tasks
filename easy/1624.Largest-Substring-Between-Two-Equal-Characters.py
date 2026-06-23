"""
1624. Largest Substring Between Two Equal Characters

Given a string s, return the length of the longest substring between two equal characters, excluding the two
characters. If there is no such substring return -1.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.

Example 2:
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".

Example 3:
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.

Constraints:
1 <= s.length <= 300
s contains only lowercase English letters.

Hint 1
Try saving the first and last position of each character

Hint 2
Try finding every pair of indexes with equal characters
"""


# Time complexity: O(n)
# Space complexity: O(1)
def maxLengthBetweenEqualCharacters(s: str) -> int:
    first = {}
    last = {}
    for i, c in enumerate(s):
        if c not in first:
            first[c] = i
        last[c] = i

    ans = -1
    for c in first:
        ans = max(ans, last[c] - first[c] - 1)
    return ans


assert maxLengthBetweenEqualCharacters("aa") == 0
assert maxLengthBetweenEqualCharacters("abca") == 2
assert maxLengthBetweenEqualCharacters("cbzxy") == -1
