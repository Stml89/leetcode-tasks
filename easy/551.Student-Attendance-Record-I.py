"""
551. Student Attendance Record I
You are given a string s representing an attendance record for a student where each character signifies
whether the student was absent, late, or present on that day. The record only contains the following three characters:
'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:
The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

Example 1:
Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.

Example 2:
Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

Constraints:
1 <= s.length <= 1000
s[i] is either 'A', 'L', or 'P'.
"""
def checkRecord(s: str) -> bool:
    # if re.search(r'L{3}', s) or len(re.findall(r'A', s)) >= 2:
    #     return False
    # return True

    a_cnt = 0

    for c in s:
        if c == 'A':
            a_cnt += 1

    if a_cnt > 1:
        return False

    l_cnt = 0

    for c in s:
        if c == 'L':
            l_cnt += 1
            if l_cnt > 2:
                return False
        else:
            l_cnt = 0
    return True


assert checkRecord("PPALLP")
assert not checkRecord("PPALLL")
assert not checkRecord("APAPAL")
assert not checkRecord("AA")
