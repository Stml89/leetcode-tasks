"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.


Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
"""
from typing import List


# Time complexity: O(n)
# Space complexity: O(n)
def fizzBuzz(n: int) -> List[str]:
    result = []
    count = 1
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            result.append("FizzBuzz")
        elif count % 5 == 0:
            result.append("Buzz")
        elif count % 3 == 0:
            result.append("Fizz")
        else:
            result.append(str(count))
        count += 1
    return result


assert fizzBuzz(3) == ["1", "2", "Fizz"]
assert fizzBuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzBuzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14",
                        "FizzBuzz"]
