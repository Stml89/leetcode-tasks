"""
1640. Check Array Formation Through Concatenation

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in
pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are
not allowed to reorder the integers in each array pieces[i].
Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]

Example 2:
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].

Example 3:
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]

Constraints:
1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
The integers in arr are distinct.
The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

Hint 1
Note that the distinct part means that every position in the array belongs to only one piece

Hint 2
Note that you can get the piece every position belongs to naively
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def canFormArray(arr: List[int], pieces: List[List[int]]) -> bool:
    pieces_dict = {piece[0]: piece for piece in pieces}
    i = 0
    while i < len(arr):
        if arr[i] not in pieces_dict:
            return False
        piece = pieces_dict[arr[i]]
        for num in piece:
            if arr[i] != num:
                return False
            i += 1
    return True


assert canFormArray(arr=[15, 88], pieces=[[88], [15]]) is True
assert canFormArray(arr=[49, 18, 16], pieces=[[16, 18, 49]]) is False
assert canFormArray(arr=[91, 4, 64, 78], pieces=[[78], [4, 64], [91]]) is True
