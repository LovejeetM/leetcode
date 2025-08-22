"""
Problem 37:

258. Add Digits
Easy
Topics
premium lock icon
Companies
Hint
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
 

Constraints:

0 <= num <= 231 - 1
"""

def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    a = list(str(num))
    n= 0
    while True:
        for i in a:
            n += int(i)
        a = list(str(n))
        n = 0
        
        if len(a)== 1:
            break
    return int(a[0])

num = 38
print(addDigits(num))