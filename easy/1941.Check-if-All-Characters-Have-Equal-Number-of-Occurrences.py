"""
1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, return true if s is a good string, or false otherwise.
A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).

Example 1:
Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

Example 2:
Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

Constraints:
1 <= s.length <= 1000
s consists of lowercase English letters.

Hint 1
Build a dictionary containing the frequency of each character appearing in s

Hint 2
Check if all values in the dictionary are the same.
"""
from collections import Counter


# Time Complexity: O(n)
# Space Complexity: O(k)
def areOccurrencesEqual(s: str) -> bool:
    freq = Counter(s)
    return len(set(freq.values())) == 1


assert areOccurrencesEqual("abacbc") is True
assert areOccurrencesEqual("aaabb") is False
assert areOccurrencesEqual("a") is True
assert areOccurrencesEqual("aaaa") is True
assert areOccurrencesEqual("aabbcc") is True
assert areOccurrencesEqual("aabbccc") is False
assert areOccurrencesEqual("abcde") is True
