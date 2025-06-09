""" # TODO example
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:
Input: word = "USA"
Output: true

Example 2:
Input: word = "FlaG"
Output: false

Constraints:
1 <= word.length <= 100
word consists of lowercase and uppercase English letters.
"""


def detectCapitalUse(word: str) -> bool:
    if word.islower() or word.isupper() or word.istitle():
        return True
    return False


# -------
# cnt = sum(c.isupper() for c in word)
#
# return cnt == len(word) \
#     or cnt == 0 \
#     or cnt == 1 and word[0].isupper()
# -------
# return word==word.upper() or word==word.capitalize() or word==word.lower()
# -------

assert detectCapitalUse("USA")
assert not detectCapitalUse("FlaG")
assert detectCapitalUse("Minsk")
