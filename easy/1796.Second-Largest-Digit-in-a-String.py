"""
1796. Second Largest Digit in a String

Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.
An alphanumeric string is a string consisting of lowercase English letters and digits.

Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The digits that appear in s are [1]. There is no second largest digit.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and digits.

Hint 1
First of all, get the distinct characters since we are only interested in those
Hint 2
Let's note that there might not be any digits.
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def secondHighest(s: str) -> int:
    largest = -1
    second_largest = -1

    for char in s:
        if not char.isdigit():
            continue

        digit = int(char)

        if digit > largest:
            second_largest = largest
            largest = digit
        elif largest > digit > second_largest:
            second_largest = digit

    return second_largest


assert secondHighest("dfa12321afd") == 2
assert secondHighest("abc1111") == -1
assert secondHighest("ck077") == 0
