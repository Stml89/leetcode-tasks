"""
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the
length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def longestPalindrome(s: str) -> int:
    count = 0
    unique = set()
    for i in s:
        if i in unique:
            unique.remove(i)
            count += 2
        else:
            unique.add(i)

    if len(unique) >= 1:
        count += 1

    return count


# Time complexity: O(n)
# Space complexity: O(n)
def longestPalindrome1(s: str) -> int:
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d.setdefault(i, 1)

    count = 0
    is_odd = False
    for freq in d.values():
        if freq % 2 == 0:
            count += freq
        else:
            count += freq - 1
            is_odd = True
    if is_odd:
        count += 1
    return count


assert longestPalindrome("abccccdd") == 7
assert longestPalindrome("a") == 1
assert longestPalindrome("bb") == 2
assert longestPalindrome("bananas") == 5
assert longestPalindrome("ababababa") == 9
