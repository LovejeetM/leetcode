"""
Problem: 

1. Two Sum
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""


def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #nums.length = 3
        if not (2 <= len(nums) <= 100000000):
            raise ValueError
        index_tocheck= 0
        n = 1
        while True: 
            if (nums[index_tocheck]+nums[n] == target):
                return [index_tocheck, n]
            else:
                if n == (len(nums)-1):
                    index_tocheck += 1
                    n = index_tocheck
            n+=1
            
m = [5,8,7,9,7,8,7,2]
t= 11
a = twoSum(m, t)
print(a)
#len(nums) = 3

#Top solution:

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in visited:
                return [i, visited[res]]
            visited[nums[i]] = i
        return [-1, -1]