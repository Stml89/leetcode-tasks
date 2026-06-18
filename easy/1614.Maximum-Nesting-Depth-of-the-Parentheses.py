"""
1614. Maximum Nesting Depth of the Parentheses

Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.

Example 1:
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation:
Digit 8 is inside of 3 nested parentheses in the string.

Example 2:
Input: s = "(1)+((2))+(((3)))"
Output: 3
Explanation:
Digit 3 is inside of 3 nested parentheses in the string.

Example 3:
Input: s = "()(())((()()))"
Output: 3

Constraints:
1 <= s.length <= 100
s consists of digits 0-9 and characters '+', '-', '*', '/', '(', and ')'.
It is guaranteed that parentheses expression s is a VPS.

Hint 1
The depth of any character in the VPS is the ( number of left brackets before it ) -
( number of right brackets before it )
"""


# Time complexity: O(n)
# Space complexity: O(1)
def maxDepth(s: str) -> int:
    current_depth = 0
    max_depth = 0
    for i in s:
        if i == '(':
            current_depth += 1
        elif i == ')':
            max_depth = max(current_depth, max_depth)
            current_depth -= 1
    return max_depth


assert maxDepth("(1+(2*3)+((8)/4))+1") == 3
assert maxDepth("(1)+((2))+(((3)))") == 3
assert maxDepth("()(())((()()))") == 3





