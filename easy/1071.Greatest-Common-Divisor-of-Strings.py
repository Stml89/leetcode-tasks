"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

Hint 1
The greatest common divisor must be a prefix of each string, so we can try all prefixes.
"""


# Time complexity: O(min(M, N) * log(min(M, N)))
# Space complexity: O(1)
def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    return str1[:gcd(len(str1), len(str2))]


assert gcdOfStrings(str1="ABCABC", str2="ABC") == "ABC"
assert gcdOfStrings(str1="ABABAB", str2="ABAB") == "AB"
assert gcdOfStrings(str1="LEET", str2="CODE") == ""
assert gcdOfStrings(str1="AAAAAA", str2="AAA") == "AAA"
assert gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX", str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX"
