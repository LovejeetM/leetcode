"""
Problem 5

5. Longest Palindromic Substring
Medium
Topics
Companies
Hint
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
"""

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        s = str(s)
        if len(s) == 1:
            return s[0]
        if s == s[::-1]: 
            return s
        store= []
        for i, char in enumerate(s):
            check = 0
            match = s[::-1]
            match1 = s[::-1]
            rev_ind = 0
            while check < len(s):     
                combined= char
                if char == match1[0]:
                    if (0 <=(rev_ind+1)<len(match)) and (0 <=(i+1)<len(s)) and s[i+1] == match[rev_ind+1]:
                        ct = 1
                        while (0 <=(rev_ind+ct)<len(match)) and (0 <=(i+ct)<len(s)) and s[i+ct] == match[rev_ind+ct]:    
                            combined = combined+s[i+ct]
                            ct += 1
                        if combined == combined[::-1]:
                            store.append(combined)
                            current_palindrome_str = combined
                            p_start_idx = i
                            p_end_idx = i + ct - 1
                            
                            while True:
                                new_start_idx = p_start_idx - 1
                                new_end_idx = p_end_idx + 1
                                
                                if new_start_idx >= 0 and new_end_idx < len(s) and \
                                   s[new_start_idx] == s[new_end_idx]:
                                    
                                    current_palindrome_str = s[new_start_idx] + current_palindrome_str + s[new_end_idx]
                                    store.append(current_palindrome_str)
                                    p_start_idx = new_start_idx
                                    p_end_idx = new_end_idx
                                else:
                                    break
                        combined = char
                    elif (0<=(rev_ind-1)<len(match)) and (0 <=(i-1)<len(s)) and s[i-1] == match[rev_ind-1]:
                        ct = 1
                        while (0 <=(rev_ind-ct)<len(match)) and (0 <=(i-ct)<len(s)) and s[i-ct] == match[rev_ind-ct]:    
                            combined = combined+s[i-ct]
                            ct += 1
                        if combined == combined[::-1]:
                            store.append(combined)
                            current_palindrome_str = combined
                            p_start_idx = i - ct + 1
                            p_end_idx = i
                            
                            while True:
                                new_start_idx = p_start_idx - 1
                                new_end_idx = p_end_idx + 1
                                
                                if new_start_idx >= 0 and new_end_idx < len(s) and \
                                   s[new_start_idx] == s[new_end_idx]:
                                    
                                    current_palindrome_str = s[new_start_idx] + current_palindrome_str + s[new_end_idx]
                                    store.append(current_palindrome_str)
                                    p_start_idx = new_start_idx
                                    p_end_idx = new_end_idx
                                else:
                                    break
                        combined = char
                    check += 1
                    rev_ind+=1
                    match1 = match1[1:]
                else:
                    check += 1
                    rev_ind+=1
                    match1 = match1[1:]
                    continue
        if not store == []: 
            pl = max(store, key=len)
            return pl
        else:
            pl = s[0]
            return pl

s = "kjjnefwojoowiaabb"  
st= longestPalindrome(s)
print(st)






def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        s = str(s)
        if len(s) == 1:
            return s[0]
        store= []
        for i, char in enumerate(s):
            check = 0
            match = s[::-1]
            match1 = s[::-1]
            while check < len(s): 
                combined= char
                if char == match1[0]:
                    rev_ind = match.index(char)
                    #for left
                    #first str:   "dhabal" a ind= 2
                    #first rev:   "labahd" a ind= 1
                    if (0 <=(rev_ind+1)<len(match)) and (0 <=(i+1)<len(s)) and s[i+1] == match[rev_ind+1]:
                        ct = 1
                        while (0 <=(rev_ind+ct)<len(match)) and (0 <=(i+ct)<len(s)) and s[i+ct] == match[rev_ind+ct]:    
                            combined = combined+s[i+ct]
                            ct += 1
                        store.append(combined)
                        combined = char
                    #for right
                    elif (0<=(rev_ind-1)<len(match)) and (0 <=(i-1)<len(s)) and s[i-1] == match[rev_ind-1]:
                        ct = 1
                        while (0 <=(rev_ind-ct)<len(match)) and (0 <=(i-ct)<len(s)) and s[i-ct] == match[rev_ind-ct]:    
                            combined = combined+s[i-ct]
                            ct += 1
                        store.append(combined)
                        combined = char
                    check += 1
                    match1 = match1[1:]
                else:
                    check += 1
                    match1 = match1[1:]
                    continue
        wr = [sto for sto in store if sto == sto[::-1]]
        pl = max(wr, key=len)
        return pl
        
s = "dhaballlbcfaaa333ijfijoeuuerreammaefg88ff"
st= longestPalindrome(s)
print(st)


