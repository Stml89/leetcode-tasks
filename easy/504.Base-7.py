"""
Можно дать студентам
504. Base 7
Given an integer num, return a string of its base 7 representation.

Example 1:
Input: num = 100
Output: "202"

Example 2:
Input: num = -7
Output: "-10"

Constraints:
-107 <= num <= 107
"""


def convertToBase7(num: int) -> str:
    if num == 0:
        return "0"
    num2 = abs(num)
    s_digits = ""
    while num2:
        s_digits += str(int(num2 % 7))
        num2 //= 7
    if num < 0:
        s_digits += "-"
    return s_digits[::-1]


assert convertToBase7(100) == "202"
assert convertToBase7(-7) == "-10"
