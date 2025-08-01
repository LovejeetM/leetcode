"""
Problem 25:

77. Combinations
Medium
Topics
premium lock icon
Companies
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.
 

Constraints:

1 <= n <= 20
1 <= k <= n
"""

# def combine(n, k):
#     """
#     :type n: int
#     :type k: int
#     :rtype: List[List[int]]
#     """
#     if k == 0:
#         return [[]]
#     if k > n:
#         return []

#     current = [[i] for i in range(1, n + 1)]
#     def itr(current):
#         for i in range(1, n+1):
#             for k,j in enumerate(current):
#                     current.append(j.append(i))

#     for a in range(k):
#         itr(current)

#     print(current)
#     print(set(current))
#     return current


# print(combine(5,2))

def combine(n: int, k: int):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    if k == 0:
        return [[]]
    if k > n:
        return []

    combos = [[i] for i in range(1, n + 1)]
    
    for _ in range(k - 1):
        next_combos = []
        
        for combo in combos:
            start = combo[-1] + 1
            for num in range(start, n + 1):
                next_combos.append(combo + [num])
        
        combos = next_combos
            
    return combos

print(combine(4, 2))