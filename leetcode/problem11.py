"""
Problem 11

17. Letter Combinations of a Phone Number
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if not len(digits) >= 1:
        return []
    map1 = {
        '0': [''],
        '1': [''],
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    
    r = ['']
    for d in digits:
        temp = []
        for prefix in r:
            for i in map1[d]:
                temp.append(prefix + i)
        r = temp
    return r


a = ""
b = letterCombinations(a)
print(b)