"""
1662. Check If Two String Arrays are Equivalent

Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:
Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.

Example 2:
Input: word1 = ["a", "cb"], word2 = ["ab", "c"]
Output: false

Example 3:
Input: word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
Output: true

Constraints:
1 <= word1.length, word2.length <= 103
1 <= word1[i].length, word2[i].length <= 103
1 <= sum(word1[i].length), sum(word2[i].length) <= 103
word1[i] and word2[i] consist of lowercase letters.

Hint 1
Concatenate all strings in the first array into a single string in the given order, the same for the second array.

Hint 2
Both arrays represent the same string if and only if the generated strings are the same.
"""
from typing import List


# Time complexity: O(n + m)
# Space complexity: O(n + m)
def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
    return ''.join(word1) == ''.join(word2)


# Time complexity: O(n + m)
# Space complexity: O(n + m)
def arrayStringsAreEqual1(word1: List[str], word2: List[str]) -> bool:
    s1, s2 = '', ''

    for word in word1:
        s1 = s1 + word
    for word in word2:
        s2 = s2 + word

    if s1 == s2:
        return True
    return False


assert arrayStringsAreEqual(["ab", "c"], ["a", "bc"]) is True
assert arrayStringsAreEqual(["a", "cb"], ["ab", "c"]) is False
