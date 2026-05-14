"""
1539. Kth Missing Positive Number

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
Return the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length

Follow up:
Could you solve this problem in less than O(n) complexity?

Hint 1
Keep track of how many positive numbers are missing as you scan the array.
"""
from typing import List


# Time complexity: O(log n)
# Space complexity: O(1)
def findKthPositive(arr: List[int], k: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        missing_count = arr[mid] - (mid + 1)

        if missing_count < k:
            left = mid + 1
        else:
            right = mid - 1

    if left == 0:
        return k

    missing_at_right = arr[right] - (right + 1)
    return arr[right] + (k - missing_at_right)


# Time complexity: O(n)
# Space complexity: O(1)
def findKthPositive1(arr: List[int], k: int) -> int:
    missing_count = 0
    for i in range(1, arr[-1] + k + 1):
        if i not in arr:
            missing_count += 1
            if missing_count == k:
                return i
    return -1


# Time complexity: O(n+k)
# Space complexity: O(n)
def findKthPositive2(arr: List[int], k: int) -> int:
    arr_set = set(arr)
    count = k
    i = 1
    while count > 0:
        if i not in arr_set:
            count -= 1
        i += 1

    return i - 1


assert findKthPositive([2, 3, 4, 7, 11], 5) == 9
assert findKthPositive([1, 2, 3, 4], 2) == 6
