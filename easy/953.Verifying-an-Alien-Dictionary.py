"""
953. Verifying an Alien Dictionary

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if
the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

h l a b c d e f g i j  k  m  n  o  p  q  r  s  t
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

h e l l o
0 6 1 1 14

l e e t  c o  d e
1 6 6 19 4 14 5 6

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character
which is less than any other character (More info).


Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List


# # Time complexity: O(n * m)
# # Space complexity: O(1)
def isAlienSorted(words: List[str], order: str) -> bool:
    mapping = {v: i for i, v in enumerate(order)}
    for i in range(1, len(words)):
        w1, w2 = words[i - 1], words[i]
        for y in range(len(w1)):
            if y == len(w2):
                return False
            if w1[y] != w2[y]:
                if mapping[w1[y]] > mapping[w2[y]]:
                    return False
                break
    return True


# Time complexity: O(m * n * log(n))
# Space complexity: O(n + k)
def isAlienSorted1(words: List[str], order: str) -> bool:
    mapping = {v: i for i, v in enumerate(order)}
    return words == sorted(words, key=lambda word: [mapping[c] for c in word])


assert isAlienSorted(words=["hello", "leetcode"], order="hlabcdefgijkmnopqrstuvwxyz")
assert not isAlienSorted(words=["word", "world", "row"], order="worldabcefghijkmnpqstuvxyz")
assert not isAlienSorted(words=["apple", "app"], order="abcdefghijklmnopqrstuvwxyz")
assert isAlienSorted(words=["app", "apple"], order="abcdefghijklmnopqrstuvwxyz")
