"""
1668. Maximum Repeating Substring

For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence.
The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence.
If word is not a substring of sequence, word's maximum k-repeating value is 0.
Given strings sequence and word, return the maximum k-repeating value of word in sequence.

Example 1:
Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".

Example 2:
Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".

Example 3:
Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".

Constraints:
1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.

Hint 1
The constraints are low enough for a brute force approach.

Hint 2
Try every k value from 0 upwards until word is no longer k-repeating.
"""


# Time complexity: O(k * m)
# Space complexity: O(1)
def maxRepeating(sequence: str, word: str) -> int:
    k = 0
    while word * (k + 1) in sequence:
        k += 1
    return k


assert maxRepeating("ababc", "ab") == 2
assert maxRepeating("ababc", "ba") == 1
assert maxRepeating("ababc", "ac") == 0
