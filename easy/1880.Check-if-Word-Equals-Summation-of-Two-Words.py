"""
1880. Check if Word Equals Summation of Two Words

The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each letter in s, which is then converted into an integer.
- For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get 21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a' through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of targetWord, or false otherwise.

Example 1:
Input: firstWord = "acb", secondWord = "cba", targetWord = "cdb"
Output: true
Explanation:
The numerical value of firstWord is "acb" -> "021" -> 21.
The numerical value of secondWord is "cba" -> "210" -> 210.
The numerical value of targetWord is "cdb" -> "231" -> 231.
We return true because 21 + 210 == 231.

Example 2:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aab"
Output: false
Explanation:
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aab" -> "001" -> 1.
We return false because 0 + 0 != 1.

Example 3:
Input: firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
Output: true
Explanation:
The numerical value of firstWord is "aaa" -> "000" -> 0.
The numerical value of secondWord is "a" -> "0" -> 0.
The numerical value of targetWord is "aaaa" -> "0000" -> 0.
We return true because 0 + 0 == 0.

Constraints:
1 <= firstWord.length, secondWord.length, targetWord.length <= 8
firstWord, secondWord, and targetWord consist of lowercase English letters from 'a' to 'j' inclusive.

Hint 1
Convert each character of each word to its numerical value.

Hint 2
Check if the numerical values satisfies the condition.
"""
from string import ascii_lowercase


# Time Complexity: O(n)
# Space Complexity: O(n)
def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def get_value(word: str) -> int:
        return int(''.join(str(ord(char) - ord('a')) for char in word))

    return get_value(firstWord) + get_value(secondWord) == get_value(targetWord)


# Time Complexity: O(n)
# Space Complexity: O(n)
def isSumEqual1(firstWord: str, secondWord: str, targetWord: str) -> bool:
    values = {char: i for i, char in enumerate(ascii_lowercase)}

    def get_value(word: str) -> int:
        return int(''.join(str(values[char]) for char in word))

    return get_value(firstWord) + get_value(secondWord) == get_value(targetWord)


# Time Complexity: O(n)
# Space Complexity: O(1)
def isSumEqual2(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def get_value(word: str) -> int:
        result = 0

        for char in word:
            result = result * 10 + (ord(char) - ord('a'))

        return result

    return get_value(firstWord) + get_value(secondWord) == get_value(targetWord)


assert isSumEqual("acb", "cba", "cdb") is True
assert isSumEqual("aaa", "a", "aab") is False
assert isSumEqual("aaa", "a", "aaaa") is True
