"""
Problem 20:

67. Add Binary
Easy
Topics
premium lock icon
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    c = int(a, 2) + int(b, 2)
    c = bin(c)[2:]
    return str(c)


a ="1010"
b = "1011"

print(addBinary(a, b))
