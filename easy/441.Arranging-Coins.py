"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins. The last of the staircase may be incomplete.
Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
> 1
> 1 1
> 1 1

Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
> 1
> 1 1
> 1 1 1
> 1 1
"""


# Time complexity: O(sqrt(n))
# Space complexity: O(1)
def arrangeCoins(n: int) -> int:
    staircase = 0
    count = 1
    while n - count >= 0:
        n -= count
        count += 1
        staircase += 1
    return staircase


assert arrangeCoins(5) == 2
assert arrangeCoins(8) == 3
assert arrangeCoins(1) == 1
assert arrangeCoins(3) == 2
