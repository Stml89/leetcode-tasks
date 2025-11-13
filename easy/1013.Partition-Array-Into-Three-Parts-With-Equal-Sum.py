"""
1013. Partition Array Into Three Parts With Equal Sum

Given an array of integers arr, return true if we can partition the array into three non-empty parts with equal sums.
Formally, we can partition the array if we can find indexes i + 1 < j with
(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])

Example 1:
Input: arr = [0,2,1,-6,6,-7,9,1,2,0,1]
Output: true
Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

Example 2:
Input: arr = [0,2,1,-6,6,7,9,-1,2,0,1]
Output: false

Example 3:
Input: arr = [3,3,6,5,-2,2,5,1,-9,4]
Output: true
Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

Constraints:
3 <= arr.length <= 5 * 104
-104 <= arr[i] <= 104

Hint 1
If we have three parts with the same sum, what is the sum of each? If you can find the first part, can you find the second part?
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def canThreePartsEqualSum(arr: List[int]) -> bool:
    summ = sum(arr)
    if summ % 3:
        return False

    average = summ // 3
    count = accum = 0

    for a in arr:
        if count == 2:
            return True
        accum += a
        if accum == average:
            count += 1
            accum = 0

    return False


assert canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1])
assert not canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1])
assert canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4])
assert not canThreePartsEqualSum([1, -1, 1, -1])
assert canThreePartsEqualSum([0, 0, 0, 0])
