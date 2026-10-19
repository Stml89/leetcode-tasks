"""
1869. Longer Contiguous Segments of Ones than Zeros

Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest
contiguous segment of 0's in s, or return false otherwise.
- For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest
continuous segment of 0s has length 3.
Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0.
The same applies if there is no 1's.

Example 1:
Input: s = "1101"
Output: true
Explanation:
The longest contiguous segment of 1s has length 2: "1101"
The longest contiguous segment of 0s has length 1: "1101"
The segment of 1s is longer, so return true.

Example 2:
Input: s = "111000"
Output: false
Explanation:
The longest contiguous segment of 1s has length 3: "111000"
The longest contiguous segment of 0s has length 3: "111000"
The segment of 1s is not longer, so return false.

Example 3:
Input: s = "110100010"
Output: false
Explanation:
The longest contiguous segment of 1s has length 2: "110100010"
The longest contiguous segment of 0s has length 3: "110100010"
The segment of 1s is not longer, so return false.

Constraints:
1 <= s.length <= 100
s[i] is either '0' or '1'.

Hint 1
Check every possible segment of 0s and 1s.

Hint 2
Is there a way to iterate through the string to keep track of the current character and its count?
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def checkZeroOnes(s: str) -> bool:
    max_ones = 0
    max_zeros = 0

    current_ones = 0
    current_zeros = 0

    for char in s:
        if char == "1":
            current_ones += 1
            current_zeros = 0
            max_ones = max(max_ones, current_ones)
        else:
            current_zeros += 1
            current_ones = 0
            max_zeros = max(max_zeros, current_zeros)

    return max_ones > max_zeros


# Time Complexity: O(n)
# Space Complexity: O(1)
def checkZeroOnes1(s: str) -> bool:
    max_ones = 0
    max_zeros = 0

    current_char = s[0]
    current_length = 0

    for char in s:
        if char == current_char:
            current_length += 1
        else:
            if current_char == "1":
                max_ones = max(max_ones, current_length)
            else:
                max_zeros = max(max_zeros, current_length)

            current_char = char
            current_length = 1

    if current_char == "1":
        max_ones = max(max_ones, current_length)
    else:
        max_zeros = max(max_zeros, current_length)

    return max_ones > max_zeros


# Time Complexity: O(n)
# Space Complexity: O(n)
def checkZeroOnes2(s: str) -> bool:
    max_ones = max(len(segment) for segment in s.split("0"))
    max_zeros = max(len(segment) for segment in s.split("1"))

    return max_ones > max_zeros


assert checkZeroOnes("1101") is True
assert checkZeroOnes("111000") is False
assert checkZeroOnes("110100010") is False
assert checkZeroOnes("1") is True
assert checkZeroOnes("0") is False
assert checkZeroOnes("11111") is True
assert checkZeroOnes("00000") is False
assert checkZeroOnes("1010101") is True
