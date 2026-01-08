"""
1175. Prime Arrangements

Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)
(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a
product of two positive integers both smaller than it.)
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:
Input: n = 100
Output: 682289015

Constraints:
1 <= n <= 100

Hint 1
Solve the problem for prime numbers and composite numbers separately.

Hint 2
Multiply the number of permutations of prime numbers over prime indices with the number of permutations of
composite numbers over composite indices.

Hint 3
The number of permutations equals the factorial.
"""
from math import isqrt, factorial


# Time complexity: O(n log log n)
# Space complexity: O(n)
def numPrimeArrangements(n: int) -> int:
    # Time complexity: O(num)
    def factorial(num: int) -> int:
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result

    # Time complexity: O(n log log n)
    def count(n: int) -> int:
        cnt = 0
        primes = [True] * (n + 1)
        for i in range(2, n + 1):
            if primes[i]:
                cnt += 1
                for j in range(i * 2, n + 1, i):
                    primes[j] = False
        return cnt

    cnt = count(n)
    ans = factorial(cnt) * factorial(n - cnt)

    return ans % (10 ** 9 + 7)


# Time complexity: O(n * √n)
# Space complexity: O(1)
def numPrimeArrangements1(n: int) -> int:
    # Time complexity: O(num * √num)
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Time complexity: O(k)
    def factorial(k: int) -> int:
        result = 1
        for i in range(2, k + 1):
            result *= i
        return result

    MOD = 10 ** 9 + 7
    prime_count = sum(1 for i in range(1, n + 1) if is_prime(i))

    return (factorial(prime_count) * factorial(n - prime_count)) % MOD


# Time complexity: O(n * √n)
# Space complexity: O(1)
def numPrimeArrangements2(n: int) -> int:
    # Time complexity: O(n * √n)
    def is_prime(n: int) -> bool:
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return n > 1

    MOD = 10 ** 9 + 7
    p = sum(map(is_prime, range(1, n + 1)))

    return (factorial(n - p) * factorial(p)) % MOD


assert numPrimeArrangements(5) == 12
assert numPrimeArrangements(100) == 682289015
