"""
1360. Number of Days Between Two Dates

Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:
The given dates are valid dates between the years 1971 and 2100.

Hint 1
Create a function f(date) that counts the number of days from 1900-01-01 to date. How can we calculate the answer ?

Hint 2
The answer is just |f(date1) - f(date2)|.

Hint 3
How to construct f(date) ?

Hint 4
For each year from 1900 to year - 1 sum up 365 or 366 in case of leap years. Then sum up for each month the number
of days, consider the case when the current year is leap, finally sum up the days.
"""


# Time complexity: O(Y + M)
# Space complexity: O(1)
def daysBetweenDates(date1: str, date2: str) -> int:
    def f(date: str) -> int:
        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        total_days = 0
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        year, month, day = map(int, date.split('-'))
        for y in range(1900, year):
            total_days += 366 if is_leap_year(y) else 365

        for i in range(month - 1):
            total_days += days_in_month[i]

        total_days += day - 1
        return total_days

    day_count1 = f(date1)
    day_count2 = f(date2)

    return abs(day_count1 - day_count2)


assert daysBetweenDates("2019-06-29", "2019-06-30") == 1
assert daysBetweenDates("2020-01-15", "2019-12-31") == 15
assert daysBetweenDates("2009-08-18", "2080-08-08") == 25923
