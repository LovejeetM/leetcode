"""
Problem 26:

78. Subsets
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""

# def subsets(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     out= []
#     prev= [0]
#     # out.append(prev)
#     for j in range(0, len(nums)):
#         a = prev[j]


#         for i, char in enumerate(nums):
#             out.append(a + char)
#             prev.append(a + char)

#     # print(prev)
#     print(out)

# subsets([1,2,3])