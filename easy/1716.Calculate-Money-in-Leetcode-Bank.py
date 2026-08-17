"""
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.
He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more
than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:
Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:
Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd
Monday, Hercy only puts in $2.

Example 3:
Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:
1 <= n <= 1000

Hint 1
Simulate the process by keeping track of how much money Hercy is putting in and which day of the week it is, and use
this information to deduce how much money Hercy will put in the next day.
"""


# Time complexity: O(n)
# Space complexity: O(1)
def totalMoney(n: int) -> int:
    day, deposit = 0, 1
    res = 0

    while day < n:
        res += deposit
        deposit += 1
        day += 1

        if day % 7 == 0:
            deposit = 1 + day // 7

    return res


# Time complexity: O(1)
# Space complexity: O(1)
def totalMoney1(n: int) -> int:
    weeks = n // 7
    low = 28
    high = 28 + 7 * (weeks - 1)
    res = weeks * (low + high) // 2

    monday = weeks + 1
    for i in range(n % 7):
        res += i + monday

    return res


# Time complexity: O(1)
# Space complexity: O(1)
def totalMoney2(n: int) -> int:
    SUM = lambda x: (x * (x + 1)) >> 1
    weeks = n // 7
    res = SUM(weeks - 1) * 7 + weeks * SUM(7)
    res += SUM(n % 7) + weeks * (n % 7)
    return res


assert totalMoney(4) == 10
assert totalMoney(10) == 37
assert totalMoney(20) == 96
