"""
717. 1-bit and 2-bit Characters

We have two special characters:
- The first character can be represented by one bit 0.
- The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

Example 1:
Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:
Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

Hint 1
Keep track of where the next character starts. At the end, you want to know if you started on the last bit.

Constraints:
1 <= bits.length <= 1000
bits[i] is either 0 or 1.
"""
# TODO example
from typing import List


def isOneBitCharacter(bits: List[int]) -> bool:
    count = 0
    flag = False
    while count <= len(bits) - 1:
        if flag and bits[count] in [1, 0]:
            flag = False
        elif count == len(bits) - 1 and flag:
            return False
        elif count == len(bits) - 1 and not flag:
            return True
        elif bits[count] == 1:
            flag = True

        count += 1


assert isOneBitCharacter([1, 0, 0])
assert not isOneBitCharacter([1, 1, 1, 0])
assert not isOneBitCharacter([1, 0])
assert isOneBitCharacter([0, 0])
assert isOneBitCharacter([0])
assert isOneBitCharacter([1, 1, 0, 0])
