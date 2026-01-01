"""
1184. Distance Between Bus Stops

A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.
The bus goes along both directions i.e. clockwise and counterclockwise.
Return the shortest distance between the given start and destination stops.

Example 1:
0(start)----1---1(destination)
|               |
4               2
|               |
3-------3-------2
Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.

Example 2:
0(start)----1---1
|               |
4               2
|               |
3-------3-------2(destination)
Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.

Example 3:
0(start)----------1----------1
|                            |
4                            2
|                            |
3(destination)-----3---------2
Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.

Constraints:
1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4

Hint 1
Find the distance between the two stops if the bus moved in clockwise or counterclockwise directions.
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(1)
def distanceBetweenBusStops(distance: List[int], start: int, destination: int) -> int:
    clockwise = sum(distance[start:destination] if start < destination else distance[destination:start])
    counterclockwise = sum(distance) - clockwise
    return min(clockwise, counterclockwise)


assert distanceBetweenBusStops([1, 2, 3, 4], 0, 1) == 1
assert distanceBetweenBusStops([1, 2, 3, 4], 0, 2) == 3
assert distanceBetweenBusStops([1, 2, 3, 4], 0, 3) == 4
