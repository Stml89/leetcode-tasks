"""
1758. Minimum Changes To Make Alternating Binary String

You are given a string s consisting only of the characters '0' and '1'. In one operation, you can
change any '0' to '1' or vice versa.
The string is called alternating if no two adjacent characters are equal. For example, the string
"010" is alternating, while the string "0100" is not.
Return the minimum number of operations needed to make s alternating.

Example 1:
Input: s = "0100"
Output: 1
Explanation: If you change the last character to '1', s will be "0101", which is alternating.

Example 2:
Input: s = "10"
Output: 0
Explanation: s is already alternating.

Example 3:
Input: s = "1111"
Output: 2
Explanation: You need two operations to reach "0101" or "1010".

Constraints:
1 <= s.length <= 104
s[i] is either '0' or '1'.

Hint 1
Think about how the final string will look like.

Hint 2
It will either start with a '0' and be like '010101010..' or with a '1' and be like '10101010..'

Hint 3
Try both ways, and check for each way, the number of changes needed to reach it from the given string. The answer is the minimum of both ways.
"""


# Time complexity: O(n)
# Space complexity: O(1)
def minOperations(s: str) -> int:
    count_start_with_0 = 0
    for i in range(len(s)):
        expected_char = '0' if i % 2 == 0 else '1'
        if s[i] != expected_char:
            count_start_with_0 += 1

    count_start_with_1 = 0
    for i in range(len(s)):
        expected_char = '1' if i % 2 == 0 else '0'
        if s[i] != expected_char:
            count_start_with_1 += 1

    return min(count_start_with_0, count_start_with_1)


assert minOperations("0100") == 1
assert minOperations("10") == 0
assert minOperations("1111") == 2
