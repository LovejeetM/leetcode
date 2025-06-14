"""
Problem 12

2566. Maximum Difference by Remapping a Digit
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer num. You know that Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Bob can make by remapping exactly one digit in num.

Notes:

When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
Bob can remap a digit to itself, in which case num does not change.
Bob can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
 

Example 1:

Input: num = 11891
Output: 99009
Explanation: 
To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.
 

Constraints:

1 <= num <= 108
"""

def minMaxDifference(num):
    """
    :type num: int
    :rtype: int
    """
    num = str(num)
    mx = list(num)
    mn = list(num)
    condition = 0
    #max
    for i, char in enumerate(mx):
        if condition == 1 and temp == char:
            mx[i] = '9'
        elif int(char)< 9 and condition == 0:
            mx[i] = '9'
            temp = char
            condition = 1
        else:
            continue
    max1 = int("".join(mx))
    #min
    condition = 0
    for i, char in enumerate(mn):
        if condition == 1 and temp == char:
            mn[i] = '0'
        elif condition == 0:
            mn[i] = '0'
            temp = char
            condition = 1
        else:
            continue
    min1 = int("".join(mn))

    return max1-min1

a = 90
b = minMaxDifference(a)
print(b)

#Solution has 0 ms runtime and is consumes less memory