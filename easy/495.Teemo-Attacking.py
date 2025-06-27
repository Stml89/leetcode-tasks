"""
495. Teemo Attacking

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a
exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time
interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and
the poison effect will end duration seconds after the new attack.
You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at
second timeSeries[i], and an integer duration.
Return the total number of seconds that Ashe is poisoned.

Example 1:
Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.

Example 2:
Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.

Constraints:
1 <= timeSeries.length <= 104
0 <= timeSeries[i], duration <= 107
timeSeries is sorted in non-decreasing order.
"""
from typing import List


def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    ans = 0
    end = 0
    for t in timeSeries:
        if t < end:
            ans += t + duration - end
        else:
            ans += duration
        end = t + duration
    return ans
    # poisoned_duration = 0
    # prev_position = -1
    # for i in range(len(timeSeries)):
    #     poisoned_interval = (timeSeries[i] + duration - 1)
    #     if prev_position >= timeSeries[i]:
    #         poisoned_duration += poisoned_interval - prev_position
    #     else:
    #         poisoned_duration += poisoned_interval - timeSeries[i] + 1
    #     prev_position = poisoned_interval
    #
    # return poisoned_duration


assert findPoisonedDuration([1, 4], 2) == 4
assert findPoisonedDuration([1, 2], 2) == 3
assert findPoisonedDuration([1, 2, 3, 4, 5], 5) == 9
