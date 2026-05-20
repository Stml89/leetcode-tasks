"""
1556. Thousand Separator

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:
Input: n = 987
Output: "987"

Example 2:
Input: n = 1234
Output: "1.234"

Constraints:
0 <= n <= 231 - 1

Hint 1
Scan from the back of the integer and use dots to connect blocks with length 3 except the last block.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def thousandSeparator(n: int) -> str:
    s = str(n)
    result = []
    tmp = ""

    for i in range(len(s) - 1, -1, -1):
        if len(tmp) != 0 and len(tmp) % 3 == 0:
            result.append(tmp[::-1])
            tmp = ""
        tmp += s[i]
    else:
        result.append(tmp[::-1])

    return ".".join(result[::-1])


# Time complexity: O(log n)
# Space complexity: O(log n)
def thousandSeparator1(n: int) -> str:
    s = str(n)
    res = []
    for i in range(len(s) - 1, -1, -3):
        res.append(s[max(0, i - 2):i + 1])
    return '.'.join(res[::-1])


assert thousandSeparator(987) == '987'
assert thousandSeparator(1234) == '1.234'
assert thousandSeparator(123456789) == '123.456.789'
