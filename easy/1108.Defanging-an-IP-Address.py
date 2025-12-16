"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
The given address is a valid IPv4 address.
"""


# Time complexity: O(n)
# Space complexity: O(n)
def defangIPaddr(address: str) -> str:
    return address.replace(".", "[.]")


# Time complexity: O(n)
# Space complexity: O(n)
def defangIPaddr1(address: str) -> str:
    ans = ""
    for i in address:
        if i != '.':
            ans += i
        else:
            ans += "[.]"
    return ans


assert defangIPaddr("1.1.1.1") == "1[.]1[.]1[.]1"
assert defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
