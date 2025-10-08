"""
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.

Example 1:
Input: s = "ab-cd"
Output: "dc-ba"

Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:
1 <= s.length <= 100
s consists of characters with ASCII values in the range [33, 122].
s does not contain '\"' or '\\'.

Hint 1
This problem is exactly like reversing a normal string except that there are certain characters that we have to simply skip.
That should be easy enough to do if you know how to reverse a string using the two-pointer approach.
"""
from string import ascii_letters


def reverseOnlyLetters(s: str) -> str:
    spec_symb = []
    letters = []
    for i in range(len(s)):
        if s[i] not in ascii_letters:
            spec_symb.append([s[i], i])
        else:
            letters.append(s[i])
    letters = letters[::-1]
    for symb, idx in spec_symb:
        letters.insert(idx, symb)

    return "".join(letters)


assert reverseOnlyLetters("ab-cd") == "dc-ba"
assert reverseOnlyLetters("a-bC-dEf-ghIj") == "j-Ih-gfE-dCba"
assert reverseOnlyLetters("Test1ng-Leet=code-Q!") == "Qedo1ct-eeLg=ntse-T!"
