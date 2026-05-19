"""
1550. Three Consecutive Odds

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000

Hint 1
Check every three consecutive numbers in the array for parity.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def threeConsecutiveOdds(arr: List[int]) -> bool:
    for i in range(len(arr) - 2):
        if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
            return True
    return False


assert threeConsecutiveOdds([2, 6, 4, 1]) == False
assert threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]) == True
assert threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 12]) == False
