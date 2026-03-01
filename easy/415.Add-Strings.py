"""
415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Example 1:
Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:
Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:
Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:
1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.
"""
from itertools import zip_longest


def addStrings(num1: str, num2: str) -> str:
    answer = ''
    carry = False
    for a, b in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
        c = ord(a) + ord(b) - ord('0')
        if carry:
            c += 1
            carry = False
        if c > ord('9'):
            carry = True
            c = c - 10
        answer += chr(c)
    if carry:
        answer += '1'
    answer = answer.rstrip('0')
    if not answer:
        return '0'
    return ''.join(reversed(answer))


assert addStrings(num1="11", num2="123") == "134"
assert addStrings(num1="456", num2="77") == "533"
assert addStrings(num1="0", num2="0") == "0"
