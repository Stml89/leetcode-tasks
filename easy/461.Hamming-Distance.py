"""
461. Hamming Distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 231 - 1
"""


# Time complexity: O(k)
# Space complexity: O(k)
def hammingDistance(x: int, y: int) -> int:
    return bin(x ^ y).count('1')


# Time complexity: O(1)
# Space complexity: O(1)
def hammingDistance1(x: int, y: int) -> int:
    string_1 = f'{x:b}'.zfill(32)
    string_2 = f'{y:b}'.zfill(32)
    distance = 0

    for i in range(len(string_1)):
        if string_1[i] != string_2[i]:
            distance += 1

    return distance


assert hammingDistance(1, 4) == 2
assert hammingDistance(3, 1) == 1
assert hammingDistance(117, 17) == 3
assert hammingDistance(680142203, 1111953568) == 19
