"""
1945. Sum of Digits of String After Convert

You are given a string s consisting of lowercase English letters, and an integer k. Your task is to convert the 
string into an integer by a special process, and then transform it by summing its digits repeatedly k times. More 
specifically, perform the following steps:
1. Convert s into an integer by replacing each letter with its position in the alphabet (i.e. replace 'a' with 1, 'b' 
with 2, ..., 'z' with 26). 
2. Transform the integer by replacing it with the sum of its digits.
3. Repeat the transform operation (step 2) k times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
1. Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
2. Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
3. Transform #2: 17 ➝ 1 + 7 ➝ 8

Return the resulting integer after performing the operations described above.

Example 1:
Input: s = "iiii", k = 1
Output: 36

Explanation:
The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.

Example 2:
Input: s = "leetcode", k = 2
Output: 6

Explanation:
The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.

Example 3:
Input: s = "zbax", k = 2
Output: 8

Constraints:
1 <= s.length <= 100
1 <= k <= 10
s consists of lowercase English letters.

Hint 1
First, let's note that after the first transform the value will be at most 100 * 10 which is not much

Hint 2
After The first transform, we can just do the rest of the transforms by brute force
"""


# Time Complexity: O(n + k * log n)
# Space Complexity: O(n)
def getLucky(s: str, k: int) -> int:
    num = ''.join(str(ord(char) - ord('a') + 1) for char in s)

    for _ in range(k):
        num = str(sum(int(digit) for digit in num))

    return int(num)


# Time Complexity: O(n + k * log n)
# Space Complexity: O(log n)
def getLucky1(s: str, k: int) -> int:
    total = 0

    for char in s:
        value = ord(char) - ord('a') + 1

        total += value // 10 + value % 10

    for _ in range(k - 1):
        total = sum(int(digit) for digit in str(total))

    return total


# Time Complexity: O(n + k * log n)
# Space Complexity: O(log n)
def getLucky2(s: str, k: int) -> int:
    total = sum(
        sum(int(digit) for digit in str(ord(char) - ord('a') + 1))
        for char in s
    )

    for _ in range(k - 1):
        total = sum(map(int, str(total)))

    return total


assert getLucky("iiii", 1) == 36
assert getLucky("leetcode", 2) == 6
assert getLucky("zbax", 2) == 8
assert getLucky("a", 1) == 1
assert getLucky("z", 1) == 8
assert getLucky("abc", 1) == 6
assert getLucky("abc", 2) == 6
assert getLucky("zzzz", 3) == 4
