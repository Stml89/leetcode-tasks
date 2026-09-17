"""
1790. Check if One String Swap Can Make Strings Equal

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two
indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of
the strings. Otherwise, return false.

Example 1:
Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:
Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:
Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.

Hint 1
The answer is false if the number of nonequal positions in the strings is not equal to 0 or 2.
Hint 2
Check that these positions have the same set of characters.
"""


# Time Complexity: O(n)
# Space Complexity O(1)
def areAlmostEqual(s1: str, s2: str) -> bool:
    diff = []

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff.append(i)

            if len(diff) > 2:
                return False

    if not diff:
        return True

    if len(diff) != 2:
        return False

    i, j = diff

    return s1[i] == s2[j] and s1[j] == s2[i]


# Time Complexity: O(min(n, m))
# Space Complexity O(min(n, m))
def areAlmostEqual1(s1: str, s2: str) -> bool:
    diff = [(a, b) for a, b in zip(s1, s2) if a != b]

    return len(diff) == 0 or (len(diff) == 2 and diff[0] == diff[1][::-1])


# Time Complexity: O(n log n)
# Space Complexity O(n + m)
def areAlmostEqual2(s1: str, s2: str) -> bool:
    if sorted(s1) == sorted(s2):
        diff = 0
        for i, j in zip(s1, s2):
            if i != j:
                diff += 1

        if diff <= 2:
            return True
    return False


assert areAlmostEqual(s1="bank", s2="kanb") is True
assert areAlmostEqual(s1="attack", s2="defend") is False
assert areAlmostEqual(s1="kelb", s2="kelb") is True
