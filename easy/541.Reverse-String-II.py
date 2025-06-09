"""
541. Reverse String II
Given a string s and an integer k, reverse the first k characters for every 2k
characters counting from the start of the string.
If there are fewer than k characters left, reverse all of them. If there are less than 2k but
greater than or equal to k characters, then reverse the first k characters and leave the other as original.

Example 1:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Example 2:
Input: s = "abcd", k = 2
Output: "bacd"

Constraints:
1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
"""


def reverseStr(s: str, k: int) -> str:
    if len(s) < k:
        return s[::-1]
    elif k <= len(s) < 2 * k:
        t = s[:k][::-1]
        return t + s[k:]
    else:
        ss = ""
        f = True
        for i in range(0, len(s), k):
            if not f:
                ss += s[i:i + k]
                f = True
            else:
                ss += s[i:i + k][::-1]
                f = False
        return ss
        # n = len(s)
        # start = 0
        # fast = 2 * k - 1
        # while fast < n:
        #     s = s[:start] + s[start:start + k][::-1] + s[start + k:]
        #     start += 2 * k
        #     fast += 2 * k
        # end = min(start + k, n)
        # s = s[:start] + s[start:end][::-1] + s[end:n]
        # return s


assert reverseStr("abcdefg", 2) == "bacdfeg"
assert reverseStr("abcd", 2) == "bacd"
assert reverseStr("abcd", 3) == "cbad"
