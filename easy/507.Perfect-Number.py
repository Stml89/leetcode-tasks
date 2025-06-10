""" # TODO example
507. Perfect Number
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
A divisor of an integer x is an integer that can divide x evenly. Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1:
Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2:
Input: num = 7
Output: false

Constraints:
1 <= num <= 108
"""


def checkPerfectNumber(num: int) -> bool:
    # total = 0
    # half = int(num*0.5)
    # while half > 0:
    #     if num % half == 0:
    #         total += half
    #     half -= 1
    #
    # return total == num
    # ====================================
    if num == 1:
        return False
    count = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            count += i + num // i
    return num == count


assert checkPerfectNumber(28)
assert not checkPerfectNumber(7)
assert not checkPerfectNumber(2)
assert not checkPerfectNumber(120)
assert not checkPerfectNumber(99999994)
