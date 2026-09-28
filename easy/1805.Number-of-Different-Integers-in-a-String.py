"""
1805. Number of Different Integers in a String

You are given a string word that consists of digits and lowercase English letters.
You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34".
Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".
Return the number of different integers after performing the replacement operations on word.
Two integers are considered different if their decimal representations without any leading zeros are different.

Example 1:
Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

Example 2:
Input: word = "leet1234code234"
Output: 2

Example 3:
Input: word = "a1b01c001"
Output: 1
Explanation: The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.

Constraints:
1 <= word.length <= 1000
word consists of digits and lowercase English letters.

Hint 1
Try to split the string so that each integer is in a different string.
Hint 2
Try to remove each integer's leading zeroes and compare the strings to find how many of them are unique.
"""
import re


# Time Complexity: O(n), where n is the length of the input string
# Space Complexity: O(m), where m is the number of distinct integer values found
def numDifferentIntegers(word: str) -> int:
    numbers = set()

    for number in re.findall(r"\d+", word):
        normalized = number.lstrip("0") or "0"
        numbers.add(normalized)

    return len(numbers)


# Time Complexity: O(n)
# Space Complexity: O(n)
def numDifferentIntegers1(word: str) -> int:
    numbers = set()
    i = 0

    while i < len(word):
        if not word[i].isdigit():
            i += 1
            continue

        j = i
        while j < len(word) and word[j].isdigit():
            j += 1

        number = word[i:j].lstrip("0")

        if number == "":
            number = "0"

        numbers.add(number)
        i = j

    return len(numbers)


# Time Complexity: O(n)
# Space Complexity: O(n)
def numDifferentIntegers2(word: str) -> int:
    res = set()
    l = 0
    r = 0
    while r < len(word):
        if word[r].isalpha():
            r += 1
        elif word[r].isdigit():
            l = r
            while r < len(word) and word[r].isdigit():
                r += 1
            res.add(int(word[l:r]))
    return len(res)


assert numDifferentIntegers("a123bc34d8ef34") == 3
assert numDifferentIntegers("leet1234code234") == 2
assert numDifferentIntegers("a1b01c001") == 1
