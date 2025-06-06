"""
Problem 3:

13. Roman to Integer
Easy
Topics
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        r ={"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        if (len(s)==1):
            return r.get(s[0])
        i = 1
        next = s[i]
        val = 0
        c = 0
        for char in s:
            if r.get(char)>=r.get(next):
                if c==0:
                    val = val + r.get(char)
                    if not (i == (len(s)-1)) and not (i >= len(s)):
                        i+=1
                        next = s[i]
                else:
                    c = 0
                    continue
            else:
                val = val + (r.get(next) - r.get(char))
                if not (i == (len(s)-1)):
                    c = 1
                    i+=2
                    next = s[i] if i < len(s) else s[len(s)-1]
                else:
                     c = 1       
        return val
        
a = "MCMXCIV" 
print(romanToInt(a))









def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        r ={"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
        if (len(s)==1):
            return r.get(s[0])
        i = 1
        next = s[i]
        val = 0
        c = 0
        for char in s:
            if r.get(char)>=r.get(next):
                if c==0:
                    val = val + r.get(char)
                    if not (i == (len(s)-1)) and not (i >= len(s)):
                        i+=1
                        next = s[i]
                else:
                    c = 0
                    continue
            else:
                val = val + (r.get(next) - r.get(char))
                if not (i == (len(s)-1)):
                    c = 1
                    i+=2
                    next = s[i] if i < len(s) else s[len(s)-1]
                else:
                     c = 1
                # elif (i+2 == (len(s))):
                #     c = 1
                #     i+=1
                #     next = s[i]         
        return val
        
a = "M" #len=7
   #"0123456"
print(romanToInt(a))







#FASTEST:

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {
            'M':1000, 
            'D':500, 
            'C':100, 
            'L':50, 
            'X':10, 
            'V':5, 
            'I':1
        }
        
        val = [d[c] for c in s]
        sol = 0

        prev = 0
        for n in val:
            sol += n if n <= prev else n - (prev)*2 
            prev = n

        return sol
