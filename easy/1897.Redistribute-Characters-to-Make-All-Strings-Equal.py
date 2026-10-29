"""
1897. Redistribute Characters to Make All Strings Equal

You are given an array of strings words (0-indexed).
In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, 
and move any character from words[i] to any position in words[j].
Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.

Example 2:
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
 
Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.

Hint 1
Characters are independent—only the frequency of characters matters.

Hint 2
It is possible to distribute characters if all characters can be divided equally among all strings.
"""
from collections import Counter


# Time Complexity: O(n * m)
# Space Complexity: O(1)
def makeEqual(words: list[str]) -> bool:
    total = Counter()

    for word in words:
        total.update(word)

    return all(count % len(words) == 0 for count in total.values())


# Time Complexity: O(n * m)
# Space Complexity: O(1)
def makeEqual1(words: list[str]) -> bool:
    counts = [0] * 26

    for word in words:
        for char in word:
            counts[ord(char) - ord('a')] += 1

    n = len(words)

    return all(count % n == 0 for count in counts)


# Time Complexity: O(n * m)
# Space Complexity: O(1)
def makeEqual(words: list[str]) -> bool:
    n = len(words)

    return all(
        sum(word.count(char) for word in words) % n == 0
        for char in 'abcdefghijklmnopqrstuvwxyz'
    )


assert makeEqual(["abc", "aabc", "bc"]) is True
assert makeEqual(["ab", "a"]) is False
assert makeEqual(["a", "a", "a"]) is True
assert makeEqual(["a", "b", "c"]) is False
assert makeEqual(["aa", "aa", "aa"]) is True
assert makeEqual(["abc", "abc", "abc"]) is True
