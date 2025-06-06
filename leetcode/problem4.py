"""
Problem 4:

3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        mylist = []
        c = 0
        m = 0
        for i, char in enumerate(s):
            if char not in mylist:
                mylist.append(char)
                c += 1
                last = char
            else:
                if m < c:
                    m = c
                
                prev = mylist.index(char)
                mylist = mylist[prev+1:]
                mylist.append(char)
                c = len(mylist)
                
        if m < c:
            m = c
        return m

a = "daaaaaaa"
print(lengthOfLongestSubstring(a))