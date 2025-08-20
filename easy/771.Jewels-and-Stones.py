"""
771. Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, and stones
representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Hint 1
For each stone, check if it is a jewel.

Constraints:
1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""


# TODO example
def numJewelsInStones(jewels: str, stones: str) -> int:
    cnt = 0
    for stone in stones:
        if stone in jewels:
            cnt += 1

    return cnt


def numJewelsInStones1(jewels: str, stones: str) -> int:
    cnt = 0
    for item in jewels:
        if item in stones:
            cnt += stones.count(item)


assert numJewelsInStones(jewels="aA", stones="aAAbbbb") == 3
assert numJewelsInStones(jewels="z", stones="ZZ") == 0
