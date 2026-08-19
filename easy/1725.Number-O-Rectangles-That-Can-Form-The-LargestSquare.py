"""
1725. Number Of Rectangles That Can Form The Largest Square

You are given an array rectangles where rectangles[i] = [li, wi] represents the ith rectangle of length li and width wi.
You can cut the ith rectangle to form a square with a side length of k if both k <= li and k <= wi. For example,
if you have a rectangle [4,6], you can cut it to get a square with a side length of at most 4.
Let maxLen be the side length of the largest square you can obtain from any of the given rectangles.
Return the number of rectangles that can make a square with a side length of maxLen.

Example 1:
Input: rectangles = [[5,8],[3,9],[5,12],[16,5]]
Output: 3
Explanation: The largest squares you can get from each rectangle are of lengths [5,3,5,5].
The largest possible square is of length 5, and you can get it out of 3 rectangles.

Example 2:
Input: rectangles = [[2,3],[3,7],[4,3],[3,7]]
Output: 3

Constraints:
1 <= rectangles.length <= 1000
rectangles[i].length == 2
1 <= li, wi <= 109
li != wi

Hint 1
What is the length of the largest square the can be cut out of some rectangle? It'll be equal to min(rectangle.length, rectangle.width). Replace each rectangle with this value.

Hint 2
Calculate maxSize by iterating over the given rectangles and maximizing the answer with their values denoted in the first hint.

Hint 3
Then iterate again on the rectangles and calculate the number whose values = maxSize.
"""
from collections import Counter
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def countGoodRectangles(rectangles: List[List[int]]) -> int:
    max_len = 0
    count = 0

    for l, w in rectangles:
        side_length = min(l, w)
        if side_length > max_len:
            max_len = side_length
            count = 1
        elif side_length == max_len:
            count += 1

    return count


# Time complexity: O(n + k log k)
# Space complexity: O(k)
def countGoodRectangles1(rectangles: List[List[int]]) -> int:
    return sorted(Counter([min(i) for i in rectangles]).items(), key=lambda x: x[0], reverse=True)[0][1]


assert countGoodRectangles([[5, 8], [3, 9], [5, 12], [16, 5]]) == 3
assert countGoodRectangles([[2, 3], [3, 7], [4, 3], [3, 7]]) == 3
