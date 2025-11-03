"""
989. Add to Array-Form of Integer

The array-form of an integer num is an array representing its digits in left to right order.
- For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:
1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104
"""
from typing import List


# Time complexity: O(log n) or O(n)
# Space complexity: O(1)
def addToArrayForm(num: List[int], k: int) -> List[int]:
    num.reverse()
    i = 0
    while k:
        d = k % 10
        if i < len(num):
            num[i] += d
        else:
            num.append(d)
        carry = num[i] // 10
        num[i] %= 10
        k //= 10
        k += carry
        i += 1
    num.reverse()

    return num


assert addToArrayForm(num=[1, 2, 0, 0], k=34) == [1, 2, 3, 4]
assert addToArrayForm(num=[2, 7, 4], k=181) == [4, 5, 5]
assert addToArrayForm(num=[2, 1, 5], k=806) == [1, 0, 2, 1]
