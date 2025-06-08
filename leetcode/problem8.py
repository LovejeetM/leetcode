"""
Problem 8:

20. Valid Parentheses
Easy
Topics
premium lock icon
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        br = list(s)
        dict1 = {
                "(":")",
                "{":"}",
                "[":"]"
        }
        temp = []

        for char in br:
            if char in dict1:
                temp.append(char)
            else:
                if len(temp) != 0 and dict1[temp.pop()] == char:
                    continue
                else:
                    return False
        
        if len(temp) != 0:
            return False
        return True

a = "{{(([[]])}}"
print(isValid(a))

# Solution runs at 0 ms runtime and beats 100% of solutions, but is uses more memory