"""
168. Excel Sheet Column Title

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...

Example 1:
Input: columnNumber = 1
Output: "A"

Example 2:
Input: columnNumber = 28
Output: "AB"

Example 3:
Input: columnNumber = 701
Output: "ZY"

Constraints:
1 <= columnNumber <= 231 - 1
"""


# Time complexity: O(log(n))
# Space complexity: O(log(n))
def convertToTitle(columnNumber: int) -> str:
    n = columnNumber
    res = ""
    while n > 0:
        n -= 1
        res = chr(n % 26 + ord('A')) + res
        n //= 26

    return res


assert convertToTitle(1) == "A"
assert convertToTitle(28) == "AB"
assert convertToTitle(701) == "ZY"
assert convertToTitle(2147483647) == "FXSHRXW"
