"""
1408. String Matching in an Array

Given an array of string words, return all strings in words that are a substring of another word. You can return the answer in any order.

Example 1:
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.

Example 2:
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".

Example 3:
Input: words = ["blue","green","bu"]
Output: []
Explanation: No string of words is substring of another string.

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 30
words[i] contains only lowercase English letters.
All the strings of words are unique.

Hint 1
Bruteforce to find if one string is substring of another or use KMP algorithm.
"""
from typing import List


# Time complexity: O(n^2 * m * k) in the worst case.
# Space complexity: O(n * m).
def stringMatching(words: List[str]) -> List[str]:
    ans = []
    for word in words:
        for word2 in words:
            if word != word2 and word in word2:
                ans.append(word)
                break

    return ans


assert stringMatching(["mass", "as", "hero", "superhero"]) == ["as", "hero"]
assert stringMatching(["leetcode", "et", "code"]) == ["et", "code"]
assert stringMatching(["blue", "green", "bu"]) == []
assert stringMatching(["a", "b", "c", "ab", "bc", "abc"]) == ["a", "b", "c", "ab", "bc"]
assert stringMatching(["a", "b", "c", "d", "e"]) == []
assert stringMatching(["a", "ab", "abc", "abcd"]) == ["a", "ab", "abc"]
assert stringMatching(["abc", "def", "ghi"]) == []
assert stringMatching(["abc", "def", "abcd"]) == ["abc"]
