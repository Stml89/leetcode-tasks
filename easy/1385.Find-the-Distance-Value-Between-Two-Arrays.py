"""
1385. Find the Distance Value Between Two Arrays

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example 1:
Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation:
For arr1[0]=4 we have:
|4-10|=6 > d=2
|4-9|=5 > d=2
|4-1|=3 > d=2
|4-8|=4 > d=2
For arr1[1]=5 we have:
|5-10|=5 > d=2
|5-9|=4 > d=2
|5-1|=4 > d=2
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

Example 2:
Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
Output: 2

Example 3:
Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
Output: 1

Constraints:
1 <= arr1.length, arr2.length <= 500
-1000 <= arr1[i], arr2[j] <= 1000
0 <= d <= 100

Hint 1
Sort 'arr2' and use binary search to get the closest element for each 'arr1[i]', it gives a time complexity of O(nlogn).
"""
from bisect import bisect_left
from typing import List


# Time complexity: O(n log n + m log n)
# Space complexity: O(1)
def findTheDistanceValue(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    count = 0

    for num in arr1:
        left, right = 0, len(arr2) - 1
        is_valid = True

        while left <= right:
            mid = (left + right) // 2

            if abs(num - arr2[mid]) <= d:
                is_valid = False
                break
            elif arr2[mid] < num:
                left = mid + 1
            else:
                right = mid - 1

        if is_valid:
            count += 1

    return count


# Time complexity: O(n log n + m log n)
# Space complexity: O(1)
def findTheDistanceValue1(arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    distance_value_count = 0

    for num in arr1:
        left_bound_index = bisect_left(arr2, num - d)
        is_valid = (left_bound_index == len(arr2) or arr2[left_bound_index] > num + d)
        distance_value_count += is_valid

    return distance_value_count


assert findTheDistanceValue([4, 5, 8], [10, 9, 1, 8], 2) == 2
assert findTheDistanceValue([1, 4, 2, 3], [-4, -3, 6, 10, 20, 30], 3) == 2
assert findTheDistanceValue([2, 1, 100, 3], [-5, -2, 10, -3, 7], 6) == 1
