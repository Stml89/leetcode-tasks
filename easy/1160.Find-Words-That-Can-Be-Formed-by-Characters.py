"""
1160. Find Words That Can Be Formed by Characters

You are given an array of strings words and a string chars.
A string is good if it can be formed by characters from chars (each character can only be used once for each word in words).
Return the sum of lengths of all good strings in words.

Example 1:
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

Example 2:
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

Constraints:
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.

Hint 1
Solve the problem for each string in words independently.

Hint 2
Now try to think in frequency of letters.

Hint 3
Count how many times each character occurs in string chars.

Hint 4
To form a string using characters from chars, the frequency of each character in chars must be greater than or equal the frequency of that character in the string to be formed.
"""
from collections import Counter
from typing import List


# Time complexity: O(N * M) where N is the number of words and M total length of the words
# Space complexity: O(K + M) where K is the length of chars and K is the maximum length of a word in words
def countCharacters(words: List[str], chars: str) -> int:
    char_count = Counter(chars)
    total_length = 0

    for word in words:
        word_count = Counter(word)
        if all(word_count[c] <= char_count[c] for c in word_count):
            total_length += len(word)

    return total_length


assert countCharacters(["cat", "bt", "hat", "tree"], "atach") == 6
assert countCharacters(["hello", "world", "leetcode"], "welldonehoneyr") == 10
