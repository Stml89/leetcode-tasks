"""
1784. Check if Binary String Has at Most One Segment of Ones

Given a binary string s without leading zeros, return true if s contains at most one contiguous segment of ones.
Otherwise, return false.

Example 1:
Input: s = "1001"
Output: false
Explanation: The string has two segments of size 1.

Example 2:
Input: s = "110"
Output: true

Constraints:
1 <= s.length <= 100
s[i] is either '0' or '1'.
s[0] is '1'.

Hint 1
It's guaranteed to have at least one segment
Hint 2
The string size is small so you can count all segments of ones with no that have no adjacent ones.
"""


# Time Complexity: O(n)
# Space Complexity O(1)
def checkOnesSegment(s: str) -> bool:
    return "01" not in s


# Time Complexity: O(n)
# Space Complexity O(1)
def checkOnesSegment1(s: str) -> bool:
    seen_zero = False

    for char in s:
        if char == "0":
            seen_zero = True
        elif seen_zero:
            return False

    return True


assert checkOnesSegment("1001") is False
assert checkOnesSegment("110") is True
