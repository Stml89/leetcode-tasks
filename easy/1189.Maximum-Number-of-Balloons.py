"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1

Example 2:
Input: text = "loonbalxballpoon"
Output: 2

Example 3:
Input: text = "leetcode"
Output: 0

Constraints:
1 <= text.length <= 104
text consists of lower case English letters only.

Hint 1
Count the frequency of letters in the given string.
Hint 2
Find the letter than can make the minimum number of instances of the word "balloon".
"""
from collections import Counter


# Time complexity: O(n)
# Space complexity: O(1)
def maxNumberOfBalloons(text: str) -> int:
    count = Counter(text)
    return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])


assert maxNumberOfBalloons("nlaebolko") == 1
assert maxNumberOfBalloons("loonbalxballpoon") == 2
assert maxNumberOfBalloons("leetcode") == 0
