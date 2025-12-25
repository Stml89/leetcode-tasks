"""
1154. Day of the Year

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
Input: date = "2019-01-09"
Output: 9

Example 2:
Input: date = "2019-02-10"
Output: 41

Example 3:
Input: date = "2003-03-01"
Output: 60

Example 4:
Input: date = "2004-03-01"
Output: 61

Constraints:
- date.length == 10
- date[4] == date[7] == '-', and all other date[i]'s are digits
- date represents a calendar date between Jan 1st, 1900 and Dec 31st, 2019.

Hint 1
Have a integer array of how many days there are per month. February gets one extra day if its a leap year.
Then, we can manually count the ordinal as day + (number of days in months before this one).
"""


# Time complexity: O(1)
# Space complexity: O(1)
def dayOfYear(date: str) -> int:
    leap_year = 0
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = date.split("-")
    year, month, day = int(year), int(month), int(day)
    if month > 2 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_year = 1

    return day + sum(days[:month - 1]) + leap_year


assert dayOfYear("2019-01-09") == 9
assert dayOfYear("2019-02-10") == 41
assert dayOfYear("2003-03-01") == 60
assert dayOfYear("2004-03-01") == 61
assert dayOfYear("1900-03-01") == 60
assert dayOfYear("1992-03-01") == 61
