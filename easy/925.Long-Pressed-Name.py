"""
925. Long Pressed Name

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.
You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.

Example 1:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.

Example 2:
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.

Constraints:
1 <= name.length, typed.length <= 1000
name and typed consist of only lowercase English letters.
"""


# Time complexity: O(n)
# Space complexity: O(1)
def isLongPressedName(name: str, typed: str) -> bool:
    cnt = 0
    for i in range(len(typed)):
        if cnt < len(name) and typed[i] == name[cnt]:
            cnt += 1
        elif cnt == 0 or typed[i] != name[cnt - 1]:
            return False

    return cnt == len(name)


# Time complexity: O(n)
# Space complexity: O(1)
def isLongPressedName1(name: str, typed: str) -> bool:
    i, j = 0, 0

    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            j += 1
        else:
            return False

    return i == len(name)


assert isLongPressedName(name="alex", typed="aaleex")
assert not isLongPressedName(name="saeed", typed="ssaaedd")
assert isLongPressedName(name="leelee", typed="lleeelee")
assert not isLongPressedName(name="xnhtq", typed="xhhttqq")
assert not isLongPressedName(name="rick", typed="kric")
