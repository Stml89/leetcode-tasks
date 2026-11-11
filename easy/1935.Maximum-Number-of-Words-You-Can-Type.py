"""
1935. Maximum Number of Words You Can Type

There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.
Given a string text of words separated by a single space (no leading or trailing spaces) 
and a string brokenLetters of all distinct letter keys that are broken, return the number of 
words in text you can fully type using this keyboard.


Example 1:
Input: text = "hello world", brokenLetters = "ad"
Output: 1
Explanation: We cannot type "world" because the 'd' key is broken.

Example 2:
Input: text = "leet code", brokenLetters = "lt"
Output: 1
Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.

Example 3:
Input: text = "leet code", brokenLetters = "e"
Output: 0
Explanation: We cannot type either word because the 'e' key is broken.
 
Constraints:
1 <= text.length <= 104
0 <= brokenLetters.length <= 26
text consists of words separated by a single space without any leading or trailing spaces.
Each word only consists of lowercase English letters.
brokenLetters consists of distinct lowercase English letters.

Hint 1
Check each word separately if it can be typed.

Hint 2
A word can be typed if all its letters are not broken.
"""


# Time Complexity: O(n + m)
# Space Complexity: O(k + w)
def canBeTypedWords(text: str, brokenLetters: str) -> int:
    broken = set(brokenLetters)
    count = 0

    for word in text.split():
        if not any(char in broken for char in word):
            count += 1

    return count


# Time Complexity: O(n + m)
# Space Complexity: O(k + w)
def canBeTypedWords1(text: str, brokenLetters: str) -> int:
    broken = set(brokenLetters)

    return sum(
        1 for word in text.split()
        if set(word).isdisjoint(broken)
    )


assert canBeTypedWords("hello world", "ad") == 1
assert canBeTypedWords("leet code", "lt") == 1
assert canBeTypedWords("leet code", "e") == 0
assert canBeTypedWords("a b c", "") == 3
assert canBeTypedWords("abc def ghi", "xyz") == 3
assert canBeTypedWords("abc def ghi", "a") == 2
assert canBeTypedWords("hello", "hello") == 0
