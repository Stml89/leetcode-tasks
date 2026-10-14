"""
1859. Sorting the Sentence

A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of lowercase and uppercase English letters.
A sentence can be shuffled by appending the 1-indexed word position to each word then rearranging the words in the sentence.
- For example, the sentence "This is a sentence" can be shuffled as "sentence4 a3 is2 This1" or "is2 sentence4 This1 a3".
Given a shuffled sentence s containing no more than 9 words, reconstruct and return the original sentence.

Example 1:
Input: s = "is2 sentence4 This1 a3"
Output: "This is a sentence"
Explanation: Sort the words in s to their original positions "This1 is2 a3 sentence4", then remove the numbers.

Example 2:
Input: s = "Myself2 Me1 I4 and3"
Output: "Me Myself and I"
Explanation: Sort the words in s to their original positions "Me1 Myself2 and3 I4", then remove the numbers.


Constraints:
2 <= s.length <= 200
s consists of lowercase and uppercase English letters, spaces, and digits from 1 to 9.
The number of words in s is between 1 and 9.
The words in s are separated by a single space.
s contains no leading or trailing spaces.

Hint 1
Divide the string into the words as an array of strings

Hint 2
Sort the words by removing the last character from each word and sorting according to it
"""


# Time Complexity: O(n)
# Space Complexity: O(n)
def sortSentence(s: str) -> str:
    words = s.split()
    result = [""] * len(words)

    for word in words:
        position = int(word[-1]) - 1
        result[position] = word[:-1]

    return " ".join(result)


# Time Complexity: O(n log n)
# Space Complexity: O(n)
def sortSentence1(s: str) -> str:
    words = s.split()
    words.sort(key=lambda word: int(word[-1]))

    return " ".join(word[:-1] for word in words)


assert sortSentence("is2 sentence4 This1 a3") == "This is a sentence"
assert sortSentence("Myself2 Me1 I4 and3") == "Me Myself and I"
assert sortSentence("Hello1") == "Hello"
assert sortSentence("One1 Two2 Three3") == "One Two Three"
assert sortSentence("Three3 Two2 One1") == "One Two Three"
assert sortSentence("b2 a1 c3") == "a b c"
assert sortSentence("i9 a1 b2 c3 d4 e5 f6 g7 h8") == "a b c d e f g h i"
