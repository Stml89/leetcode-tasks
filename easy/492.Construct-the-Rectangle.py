"""
492. Construct the Rectangle

A web developer needs to know how to design a web page's size. So, given a specific rectangular web page’s area,
your job by now is to design a rectangular web page, whose length L and width W satisfy the following requirements:
- The area of the rectangular web page you designed must equal to the given target area.
- The width W should not be larger than the length L, which means L >= W.
- The difference between length L and width W should be as small as possible.
Return an array [L, W] where L and W are the length and width of the web page you designed in sequence.

Example 1:
Input: area = 4
Output: [2,2]
Explanation: The target area is 4, and all the possible ways to construct it are [1,4], [2,2], [4,1].
But according to requirement 2, [1,4] is illegal; according to requirement 3,  [4,1] is not optimal compared to
[2,2]. So the length L is 2, and the width W is 2.

Example 2:
Input: area = 37
Output: [37,1]

Example 3:
Input: area = 122122
Output: [427,286]

Hint 1:
The W is always less than or equal to the square root of the area, so we start searching at sqrt(area) till we find the result.
"""
from typing import List


def constructRectangle(area: int) -> List[int]:
    l = []
    a = int(area ** 0.5)
    for i in range(a, 0, -1):
        if area % i == 0:
            l.extend([[area // i, i]])
            break

    return l[-1]

    # for l in range(int(area ** 0.5), 0, -1):
    #     if area % l == 0:
    #         return [area // l, l]


assert constructRectangle(4) == [2, 2]
assert constructRectangle(37) == [37, 1]
assert constructRectangle(122122) == [427, 286]
