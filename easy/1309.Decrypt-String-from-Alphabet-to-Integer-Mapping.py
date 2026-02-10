"""
1309. Decrypt String from Alphabet to Integer Mapping

You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:
- Characters ('a' to 'i') are represented by ('1' to '9') respectively.
- Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.

Return the string formed after mapping.
The test cases are generated so that a unique mapping will always exist.

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

Example 2:
Input: s = "1326#"
Output: "acz"

Constraints:
1 <= s.length <= 1000
s consists of digits and the '#' letter.
s will be a valid string such that mapping is always possible.

Hint 1
Scan from right to left, in each step of the scanning check whether there is a trailing "#" 2 indexes away.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def freqAlphabets(s: str) -> str:
    result = []
    i = len(s) - 1
    while i >= 0:
        if s[i] == '#':
            number = int(s[i - 2:i])
            i -= 3
        else:
            number = int(s[i])
            i -= 1

        char = chr(number + 96)
        result.append(char)

    return ''.join(reversed(result))


assert freqAlphabets("10#11#12") == "jkab"
assert freqAlphabets("1326#") == "acz"
