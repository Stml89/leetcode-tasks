"""
476. Number Complement
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""


def findComplement(num: int) -> int:
    num_bits = num.bit_length()
    all_ones = (1 << num_bits) - 1
    return num ^ all_ones


def findComplement1(num: int) -> int:
    return num ^ (2 ** (len(bin(num)[2:])) - 1)


def findComplement2(num: int) -> int:
    b = f"{num:b}".replace("0", "2").replace("1", "0").replace("2", "1")
    return int(b, 2)


assert findComplement2(5) == 2
assert findComplement2(1) == 0
