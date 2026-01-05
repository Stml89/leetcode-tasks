"""
1185. Day of the Week

Given a date, return the corresponding day of the week for that date.
The input is given as three integers representing the day, month and year respectively.
Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
Note: January 1, 1971 was a Friday.

Example 1:
Input: day = 31, month = 8, year = 2019
Output: "Saturday"

Example 2:
Input: day = 18, month = 7, year = 1999
Output: "Sunday"

Example 3:
Input: day = 15, month = 8, year = 1993
Output: "Sunday"

Constraints:
The given dates are valid dates between the years 1971 and 2100.

Hint 1
Sum up the number of days for the years before the given year.
Hint 2
Handle the case of a leap year.
Hint 3
Find the number of days for each month of the given year.
"""
from datetime import datetime


# Time complexity: O(year - 1971 + month)
# Space complexity: O(1)
def dayOfTheWeek1(day: int, month: int, year: int) -> str:
    days_of_week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    total_days = 0

    for y in range(1971, year):
        total_days += 366 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 365

    for m in range(1, month):
        total_days += days_in_month[m - 1]
        if m > 2 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
            total_days += 1

    total_days += day - 1

    return days_of_week[total_days % 7]


def dayOfTheWeek(day: int, month: int, year: int) -> str:
    date_obj = datetime(year, month, day)
    weekday_name = date_obj.strftime('%A')

    return weekday_name


assert dayOfTheWeek(31, 8, 2019) == "Saturday"
assert dayOfTheWeek(18, 7, 1999) == "Sunday"
assert dayOfTheWeek(15, 8, 1993) == "Sunday"
assert dayOfTheWeek(1, 1, 1971) == "Friday"
assert dayOfTheWeek(29, 2, 2020) == "Saturday"
assert dayOfTheWeek(28, 2, 2021) == "Sunday"
assert dayOfTheWeek(31, 8, 2000) == "Thursday"
