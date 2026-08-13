"""
1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] =
[numberOfBoxesi, numberOfUnitsPerBoxi]:
- numberOfBoxesi is the number of boxes of type i.
- numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.
Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Constraints:
1 <= boxTypes.length <= 1000
1 <= numberOfBoxesi, numberOfUnitsPerBoxi <= 1000
1 <= truckSize <= 106

Hint 1
If we have space for at least one box, it's always optimal to put the box with the most units.

Hint 2
Sort the box types with the number of units per box non-increasingly.

Hint 3
Iterate on the box types and take from each type as many as you can.
"""
from itertools import islice, repeat
import heapq
from typing import List


# Time complexity: O(n log n), where n is the number of box types
# Space complexity: O(1)
def maximumUnits(boxTypes: List[List[int]], truckSize: int) -> int:
    # Sort the box types by number of units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        if truckSize == 0:
            break

        # Take as many boxes as possible from the current type
        boxes_to_take = min(numberOfBoxes, truckSize)
        total_units += boxes_to_take * numberOfUnitsPerBox
        truckSize -= boxes_to_take

    return total_units


# Time complexity: O(n log n), where n is the number of box types
# Space complexity: O(n)
def maximumUnits1(boxTypes: List[List[int]], truckSize: int) -> int:
    heap = []

    for numOfBoxes, noOfUnits in boxTypes:
        heapq.heappush(heap, (-noOfUnits, numOfBoxes))

    maxUnits = 0

    while heap and truckSize > 0:
        negUnits, noOfBoxes = heapq.heappop(heap)
        noOfUnits = -negUnits

        if truckSize - noOfBoxes >= 0:
            maxUnits += (noOfUnits * noOfBoxes)
            print(f"{noOfUnits},{noOfBoxes}={maxUnits}")
            truckSize -= noOfBoxes
        else:
            maxUnits += (truckSize * noOfUnits)
            truckSize -= noOfBoxes
            print(maxUnits)

    return maxUnits


# Time complexity: O(n log n + N), where n is the number of box types
# Space complexity: O(n)
def maximumUnits2(arr: List[List[int]], N: int) -> int:
    arr = sorted(arr, key=lambda t: t[1], reverse=True)
    return sum(islice((e for q, x in arr for e in repeat(x, q)), 0, N))


assert maximumUnits([[1, 3], [2, 2], [3, 1]], 4) == 8
assert maximumUnits([[5, 10], [2, 5], [4, 7], [3, 9]], 10) == 91
