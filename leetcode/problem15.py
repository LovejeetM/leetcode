"""
Problem 15

58. Length of Last Word
Easy
Topics
premium lock icon
Companies
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
Accepted
2,778,193/4.9M

"""


def lengthOfLastWord(s):
        """
        :type s: str"""
        sl= s.split(" ")
        sl = [i for i in sl if i != ""]
        return len(sl[len(sl)-1])
