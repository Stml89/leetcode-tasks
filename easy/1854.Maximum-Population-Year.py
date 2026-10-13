"""
1854. Maximum Population Year

You are given a 2D integer array logs where each logs[i] = [birthi, deathi] indicates the birth and death years of the ith person.
The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1]. Note that
the person is not counted in the year that they die.
Return the earliest year with the maximum population.

Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960
Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:
1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050

Hint 1
For each year find the number of people whose birth_i ≤ year and death_i > year.

Hint 2
Find the maximum value between all years.
"""
from typing import List


# Time Complexity: O(n + Y), where Y = 101 — years from 1950 to 2050
# Space Complexity: O(Y)
def maximumPopulation(logs: List[List[int]]) -> int:
    start_year = 1950
    end_year = 2050

    population_change = [0] * (end_year - start_year + 1)

    for birth, death in logs:
        population_change[birth - start_year] += 1
        population_change[death - start_year] -= 1

    max_population = 0
    current_population = 0
    result_year = start_year

    for i, change in enumerate(population_change):
        current_population += change

        if current_population > max_population:
            max_population = current_population
            result_year = start_year + i

    return result_year


assert maximumPopulation([[1993, 1999], [2000, 2010]]) == 1993
assert maximumPopulation([[1950, 1961], [1960, 1971], [1970, 1981]]) == 1960
assert maximumPopulation([[1950, 2050]]) == 1950  # One person
assert maximumPopulation([[2000, 2010], [2000, 2010], [2000, 2010]]) == 2000  # Everyone live in one period
assert maximumPopulation([[1950, 1960], [1960, 1970]]) == 1950  # One die, next born
assert maximumPopulation([[1950, 1952], [1951, 1953], [1960, 1962], [1961, 1963]]) == 1951
assert maximumPopulation([[1950, 1951], [1951, 1952], [1952, 1953]]) == 1950  # Short intervals
