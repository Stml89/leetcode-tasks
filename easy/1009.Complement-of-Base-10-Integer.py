"""
1009. Complement of Base 10 Integer

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the
1's to 0's in its binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

Example 1:
Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Example 2:
Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Example 3:
Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

Constraints:
0 <= n < 109

Hint 1
A binary number plus its complement will equal 111....111 in binary. Also, N = 0 is a corner case.
"""


# Time complexity: O(log n)
# Space complexity: O(log n)
def bitwiseComplement2(n: int) -> int:
    if n == 0:
        return 1
    a = bin(n)[2:]
    res = int(a.replace("0", "1")) - int(a)
    return int(f"0b{res}", 2)


# Time complexity: O(1)
# Space complexity: O(1)
def bitwiseComplement1(n: int) -> int:
    if n == 0:
        return 1
    bit_length = n.bit_length()
    mask = (1 << bit_length) - 1
    return n ^ mask


# Time complexity: O(log n)
# Space complexity: O(1)
def bitwiseComplement(n: int) -> int:
    cnt = 0
    ans = 0
    if n == 0:
        return 1
    while n > 0:
        if n & 1:
            cnt += 1
        else:
            ans = ans + (2 ** cnt)
            cnt += 1
        n = n >> 1
    return ans


assert bitwiseComplement(5) == 2
assert bitwiseComplement(7) == 0
assert bitwiseComplement(10) == 5
