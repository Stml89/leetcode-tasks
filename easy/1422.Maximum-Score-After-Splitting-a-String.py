"""
1422. Maximum Score After Splitting a String

Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty
substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3

Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.

Hint 1
Precompute a prefix sum of ones ('1').

Hint 2
Iterate from left to right counting the number of zeros ('0'), then use the precomputed prefix sum for counting ones ('1'). Update the answer.
"""


# Time complexity: O(n^2)
# Space complexity: O(1)
def maxScore(s: str) -> int:
    ans = 0
    for i in range(1, len(s)):
        zero_counter = s[:i].count('0')
        ones_counter = s[i:].count('1')
        ans = max(ans, zero_counter + ones_counter)
    return ans


# Time complexity: O(n)
# Space complexity: O(n)
def maxScore1(s: str) -> int:
    prefix_sum = [0] * (len(s) + 1)
    for i in range(1, len(s) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + (s[i - 1] == '1')

    ans = 0
    count_zero = 0
    for i in range(len(s) - 1):
        if s[i] == '0':
            count_zero += 1

        ans = max(ans, count_zero + prefix_sum[len(s)] - prefix_sum[i + 1])

    return ans


assert maxScore("00111") == 5
assert maxScore("011101") == 5
assert maxScore("1111") == 3
