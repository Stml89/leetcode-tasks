"""
1903. Largest Odd Number in String

You are given a string num, representing a large integer. Return the largest-valued odd integer 
(as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

Example 2:
Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".

Example 3:
Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
 

Constraints:
1 <= num.length <= 105

Hint 1
In what order should you iterate through the digits?

Hint 2
If an odd number exists, where must the number start from?
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def largestOddNumber(num: str) -> str:
    for i in range(len(num) - 1, -1, -1):
        if int(num[i]) % 2 == 1:
            return num[:i + 1]

    return ""


# Time Complexity: O(n)
# Space Complexity: O(1)
def largestOddNumber1(num: str) -> str:
    last_odd = -1

    for digit in "13579":
        last_odd = max(last_odd, num.rfind(digit))

    return num[:last_odd + 1]


# Time Complexity: O(n)
# Space Complexity: O(1)
def largestOddNumber2(num: str) -> str:
    for i, digit in enumerate(reversed(num)):
        if int(digit) % 2:
            return num[:len(num) - i]

    return ""


# Time Complexity: O(k), where k - number of even digits
# Space Complexity: O(1)
def largestOddNumber3(num: str) -> str:
    return num.rstrip("02468")


assert largestOddNumber("52") == "5"
assert largestOddNumber("4206") == ""
assert largestOddNumber("35427") == "35427"
assert largestOddNumber("123456") == "12345"
assert largestOddNumber("100") == "1"
assert largestOddNumber("2468") == ""
assert largestOddNumber("7") == "7"
assert largestOddNumber("11112") == "1111"
