"""
929. Unique Email Addresses

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters,
the email may contain one or more '.' or '+'.
- For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.

If you add periods '.' between some characters in the local name part of an email address, mail sent there will be
forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.
- For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.

If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain
emails to be filtered. Note that this rule does not apply to domain names.
- For example, "m.y+name@email.com" will be forwarded to "my@email.com".

It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses
that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
Domain names must contain at least one character before ".com" suffix.
"""
from typing import List


# Time complexity: O(n * m)
# Space complexity: O(n * m)
def numUniqueEmails(emails: List[str]) -> int:
    emails_to_send = []
    for email in emails:
        if email.startswith('+'):
            continue
        if 1 < email.count("@") > 1:
            continue
        if not email.endswith('.com'):
            continue

        local_name, domain_name = email.split('@')
        if len(local_name) >= 1 and len(domain_name) > 4:
            tmp_email = ""
            for char in local_name:
                if char == '.':
                    continue
                elif char == "+":
                    break
                else:
                    tmp_email += char
            emails_to_send.append(f"{tmp_email}@{domain_name}")

    return len(set(emails_to_send))


# Time complexity: O(n * m)
# Space complexity: O(n * m)
def numUniqueEmails1(emails: List[str]) -> int:
    result = set()
    for e in emails:
        un, dn = e.split('@')
        l = []
        for i in un:
            if i == '.':
                continue
            elif i == '+':
                break
            l.append(i)
        un = "".join(l)
        result.add(un + '@' + dn)
    return len(result)


assert numUniqueEmails(
    ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]) == 2
assert numUniqueEmails(["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]) == 3
