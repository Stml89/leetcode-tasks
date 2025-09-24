"""
884. Uncommon Words from Two Sentences

A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Explanation:
The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]

Constraints:
1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
# TODO example
from collections import Counter
from typing import List


def uncommonFromSentences1(s1: str, s2: str) -> List[str]:
    l = []
    ls1 = set(s1.split())
    ls2 = set(s2.split())
    s1diff = ls1.difference(ls2)
    s2diff = ls2.difference(ls1)

    for i in s1diff:
        if list(s1.split()).count(i) < 2:
            l.append(i)
    for i in s2diff:
        if list(s2.split()).count(i) < 2:
            l.append(i)

    return l


def uncommonFromSentences(s1: str, s2: str) -> List[str]:
    res = (s1 + " " + s2).split()
    cnt = Counter(res)

    return [c for c, v in cnt.items() if v == 1]


assert uncommonFromSentences(s1="this apple is sweet", s2="this apple is sour") == ["sweet", "sour"]
assert uncommonFromSentences(s1="apple apple", s2="banana") == ["banana"]
assert uncommonFromSentences(s1="op vu kux dn jsenj hbdez hbdez nbenh z op dxmqd op",
                             s2="kux wnx wnx wbi jsenj nlgfn vu f vu fvxas dn op tb") == ["nbenh", "dxmqd", "z",
                                                                                          "nlgfn", "fvxas", "f", "tb",
                                                                                          "wbi"]
