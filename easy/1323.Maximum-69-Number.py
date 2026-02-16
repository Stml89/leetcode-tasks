"""
1323. Maximum 69 Number

You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:
Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Example 2:
Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Example 3:
Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.


Constraints:
1 <= num <= 104
num consists of only 6 and 9 digits.

Hint 1
Convert the number in an array of its digits.

Hint 2
Brute force on every digit to get the maximum number.
"""


# Time complexity: O(d), where d is the number of digits
# Space complexity: O(d)
def maximum69Number(num: int) -> int:
    str_num = str(num)
    if '6' not in str_num:
        return num

    max_num = num
    for i in range(len(str_num)):
        if str_num[i] == '6':
            new_num = str_num[:i] + '9' + str_num[i + 1:]
            max_num = max(max_num, int(new_num))

    return max_num


# Time complexity: O(d), where d is the number of digits
# Space complexity: O(d)
def maximum69Number1(num: int) -> int:
    nums = list(str(num))

    for i in range(len(nums)):
        if nums[i] == '6':
            nums[i] = '9'
            break

    return int("".join(nums))


assert maximum69Number(9669) == 9969
assert maximum69Number(9996) == 9999
assert maximum69Number(9999) == 9999
