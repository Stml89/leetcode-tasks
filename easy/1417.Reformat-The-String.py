"""
1417. Reformat The String

You are given an alphanumeric string s. (Alphanumeric string is a string consisting of lowercase English letters and digits).
You have to find a permutation of the string where no letter is followed by another letter and no digit is
followed by another digit. That is, no two adjacent characters have the same type.
Return the reformatted string or return an empty string if it is impossible to reformat the string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters have the same type in "0a1b2c". "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only characters so we cannot separate them by digits.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits so we cannot separate them by characters.

Constraints:
1 <= s.length <= 500
s consists of only lowercase English letters and/or digits.

Hint 1
Count the number of letters and digits in the string. if cntLetters - cntDigits has any of the values [-1, 0, 1]
we have an answer, otherwise we don't have any answer.

Hint 2
Build the string anyway as you wish. Keep in mind that you need to start with the type that has more characters if
cntLetters ≠ cntDigits.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def reformat(s: str) -> str:
    if s.isdigit():
        return ""

    if s.isalpha():
        return ""

    digit, letter = "", ""
    for c in s:
        if c.isdigit():
            digit += c
        else:
            letter += c

    if abs(len(digit) - len(letter)) > 1:
        return ""

    ans = ""
    if len(digit) > len(letter):
        for i in range(len(letter)):
            ans += digit[i] + letter[i]
        ans += digit[-1]
    elif len(letter) > len(digit):
        for i in range(len(digit)):
            ans += letter[i] + digit[i]
        ans += letter[-1]
    else:
        for i in range(len(digit)):
            ans += letter[i] + digit[i]

    return ans


# Time complexity: O(n)
# Space complexity: O(n)
def reformat1(s: str) -> str:
    A = [c for c in s if c.isalpha()]
    B = [c for c in s if c.isdigit()]

    if len(A) < len(B):
        A, B = B, A
    if len(A) - len(B) > 1:
        return ''

    ans = []
    for i in range(len(B)):
        ans.append(A[i])
        ans.append(B[i])

    if len(A) == len(B) + 1:
        ans.append(A[-1])

    return ''.join(ans)


assert reformat("a0b1c2") == "a0b1c2"
assert reformat("leetcode") == ""
assert reformat("1229857369") == ""
