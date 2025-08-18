"""
762. Prime Number of Set Bits in Binary Representation

Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a
prime number of set bits in their binary representation.
Recall that the number of set bits an integer has is the number of 1's present when written in binary.
For example, 21 written in binary is 10101, which has 3 set bits.

Example 1:
Input: left = 6, right = 10
Output: 4
Explanation:
6  -> 110 (2 set bits, 2 is prime)
7  -> 111 (3 set bits, 3 is prime)
8  -> 1000 (1 set bit, 1 is not prime)
9  -> 1001 (2 set bits, 2 is prime)
10 -> 1010 (2 set bits, 2 is prime)
4 numbers have a prime number of set bits.

Example 2:
Input: left = 10, right = 15
Output: 5
Explanation:
10 -> 1010 (2 set bits, 2 is prime)
11 -> 1011 (3 set bits, 3 is prime)
12 -> 1100 (2 set bits, 2 is prime)
13 -> 1101 (3 set bits, 3 is prime)
14 -> 1110 (3 set bits, 3 is prime)
15 -> 1111 (4 set bits, 4 is not prime)
5 numbers have a prime number of set bits.

Hint 1
Write a helper function to count the number of set bits in a number, then check whether the number of set bits is 2, 3, 5, 7, 11, 13, 17 or 19.

Constraints:
1 <= left <= right <= 106
0 <= right - left <= 104
"""


# TODO example
def is_prime(n: int) -> bool:
    if n <= 1:
        return False

    flag = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            flag = False
            break

    return flag


def countPrimeSetBits(left: int, right: int) -> int:
    l = [i.bit_count() for i in range(left, right + 1)]
    l2 = [i for i in l if is_prime(i)]

    return len(l2)


assert countPrimeSetBits(left=6, right=10) == 4
assert countPrimeSetBits(left=10, right=15) == 5
