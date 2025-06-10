"""
Problem 9

35. Search Insert Position
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    try:
        return nums.index(target)
    except ValueError:
        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        
        if target > nums[len(nums) // 2]:
            for i in range((len(nums)// 2), len(nums)):
                if target > nums[i] and target < nums[i+1]:
                    return  i+1
                else:
                    continue
        else:
            for i in range(0, (len(nums)// 2)):
                if target > nums[i] and target < nums[i+1]:
                    return  i+1
                else:
                    continue

a = [1,2,3,4,5,7,9,9,11]
t = 10

