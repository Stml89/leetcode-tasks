"""
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words
(including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List


# Time complexity: O(n^2)
# Space complexity: O(1)
def commonChars(words: List[str]) -> List[str]:
    cnt = Counter(words[0])
    for word in range(1, len(words)):
        tmp = Counter(words[word])
        for char in cnt:
            cnt[char] = min(cnt[char], tmp[char])

    return list(cnt.elements())


# Time complexity: O(n * m)
# Space complexity: O(n)
def commonChars1(words: list[str]) -> list[str]:
    common_count = Counter(words[0])

    for word in words[1:]:
        common_count &= Counter(word)

    result = []
    for char, freq in common_count.items():
        result.extend([char] * freq)

    return result


assert commonChars(["bella", "label", "roller"]) == ["e", "l", "l"]
assert commonChars(["cool", "lock", "cook"]) == ["c", "o"]
