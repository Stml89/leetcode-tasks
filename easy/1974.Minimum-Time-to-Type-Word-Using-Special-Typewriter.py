"""
1974. Minimum Time to Type Word Using Special Typewriter

There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle with a pointer. 
A character can only be typed if the pointer is pointing to that character. The pointer is initially pointing to 
the character 'a'.

Each second, you may perform one of the following operations:

Move the pointer one character counterclockwise or clockwise.
Type the character the pointer is currently on.
Given a string word, return the minimum number of seconds to type out the characters in word.

Example 1:
Input: word = "abc"
Output: 5
Explanation: 
The characters are printed as follows:
- Type the character 'a' in 1 second since the pointer is initially on 'a'.
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer clockwise to 'c' in 1 second.
- Type the character 'c' in 1 second.

Example 2:
Input: word = "bza"
Output: 7
Explanation:
The characters are printed as follows:
- Move the pointer clockwise to 'b' in 1 second.
- Type the character 'b' in 1 second.
- Move the pointer counterclockwise to 'z' in 2 seconds.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'a' in 1 second.
- Type the character 'a' in 1 second.

Example 3:
Input: word = "zjpc"
Output: 34
Explanation:
The characters are printed as follows:
- Move the pointer counterclockwise to 'z' in 1 second.
- Type the character 'z' in 1 second.
- Move the pointer clockwise to 'j' in 10 seconds.
- Type the character 'j' in 1 second.
- Move the pointer clockwise to 'p' in 6 seconds.
- Type the character 'p' in 1 second.
- Move the pointer counterclockwise to 'c' in 13 seconds.
- Type the character 'c' in 1 second.
 
Constraints:
1 <= word.length <= 100
word consists of lowercase English letters.

Hint 1
There are only two possible directions you can go when you move to the next letter.

Hint 2
When moving to the next letter, you will always go in the direction that takes the least amount of time.
"""


# Time Complexity: O(n), where n - length of word
# Space Complexity: O(1)
def minTimeToType(word: str) -> int:
    total = 0
    current = 0

    for char in word:
        target = ord(char) - ord('a')
        distance = abs(target - current)

        total += min(distance, 26 - distance) + 1
        current = target

    return total


# Time Complexity: O(n)
# Space Complexity: O(1)
def minTimeToType1(word: str) -> int:
    total = 0
    current = 0

    for char in word:
        target = ord(char) - ord('a')
        clockwise = (target - current) % 26
        counterclockwise = (current - target) % 26

        total += min(clockwise, counterclockwise) + 1
        current = target

    return total


assert minTimeToType("abc") == 5
assert minTimeToType("bza") == 7
assert minTimeToType("zjpc") == 34
assert minTimeToType("a") == 1
assert minTimeToType("z") == 2
assert minTimeToType("az") == 3
assert minTimeToType("za") == 3
assert minTimeToType("aaaa") == 4
assert minTimeToType("abcdefghijklmnopqrstuvwxyz") == 51
