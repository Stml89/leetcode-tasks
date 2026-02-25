"""
1346. Check If N and Its Double Exist

Given an array arr of integers, check if there exist two indices i and j such that :
- i != j
- 0 <= i, j < arr.length
- arr[i] == 2 * arr[j]

Example 1:
Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]

Example 2:
Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.

Constraints:
2 <= arr.length <= 500
-103 <= arr[i] <= 103

Hint 1
Loop from i = 0 to arr.length, maintaining in a hashTable the array elements from [0, i - 1].

Hint 2
On each step of the loop check if we have seen the element 2 * arr[i] so far.

Hint 3
Also check if we have seen arr[i] / 2 in case arr[i] % 2 == 0.
"""
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(1)
def checkIfExist(arr: List[int]) -> bool:
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if i != j and arr[i] == 2 * arr[j]:
                return True
    return False


assert checkIfExist([10, 2, 5, 3])
assert not checkIfExist([3, 1, 7, 11])
assert not checkIfExist([-2, 0, 10, -19, 4, 6, -8])
assert checkIfExist([0, 0])
assert checkIfExist([7, 1, 14, 11])
