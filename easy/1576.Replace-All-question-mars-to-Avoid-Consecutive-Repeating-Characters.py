"""
1576. Replace All ?'s to Avoid Consecutive Repeating Characters

Given a string s containing only lowercase English letters and the '?' character, convert all the '?' characters
into lowercase letters such that the final string does not contain any consecutive repeating characters. You cannot
modify the non '?' characters.
It is guaranteed that there are no consecutive repeating characters in the given string except for '?'.
Return the final string after all the conversions (possibly zero) have been made. If there is more than one solution,
return any of them. It can be shown that an answer is always possible with the given constraints.

Example 1:
Input: s = "?zs"
Output: "azs"
Explanation: There are 25 solutions for this problem. From "azs" to "yzs", all are valid. Only "z" is an invalid
modification as the string will consist of consecutive repeating characters in "zzs".

Example 2:
Input: s = "ubv?w"
Output: "ubvaw"
Explanation: There are 24 solutions for this problem. Only "v" and "w" are invalid modifications as the strings
will consist of consecutive repeating characters in "ubvvw" and "ubvww".

Constraints:
1 <= s.length <= 100
s consist of lowercase English letters and '?'.

Hint 1
Processing string from left to right, whenever you get a ‘?’, check left character and right character, and
select a character not equal to either of them

Hint 2
Do take care to compare with replaced occurrence of ‘?’ when checking the left character.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def modifyString(s: str) -> str:
    s = list(s)

    for i in range(len(s)):
        if s[i] == '?':
            for c in 'abc':
                if (i > 0 and s[i - 1] == c) or (i < len(s) - 1 and s[i + 1] == c):
                    continue
                s[i] = c
                break

    return ''.join(s)


assert modifyString("") == ""
assert modifyString("?zs") == "azs"
assert modifyString("ubv?w") == "ubvaw"
assert modifyString("?") == "a"
