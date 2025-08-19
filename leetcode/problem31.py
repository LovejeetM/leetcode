"""
Problem 31:

242. Valid Anagram
Easy
Topics
premium lock icon
Companies
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

def isAnagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        

        
        dict2 = {}
        dict1 = {}
        for i in s:
            if i not in dict2:
                dict2[i] = 1
            else: 
                dict2[i] += 1

        for i in t:
             if i not in dict1:
                dict1[i] = 1
             else: 
                dict1[i] += 1

        if dict1 == dict2:
            return True
        
        return False

s = "anagrraam"
t = "nagaarram"
print(isAnagram(s, t))