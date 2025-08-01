"""
Problem 27:

3024. Type of Triangle
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.

 

Example 1:

Input: nums = [3,3,3]
Output: "equilateral"
Explanation: Since all the sides are of equal length, therefore, it will form an equilateral triangle.
Example 2:

Input: nums = [3,4,5]
Output: "scalene"
Explanation: 
nums[0] + nums[1] = 3 + 4 = 7, which is greater than nums[2] = 5.
nums[0] + nums[2] = 3 + 5 = 8, which is greater than nums[1] = 4.
nums[1] + nums[2] = 4 + 5 = 9, which is greater than nums[0] = 3. 
Since the sum of the two sides is greater than the third side for all three cases, therefore, it can form a triangle.
As all the sides are of different lengths, it will form a scalene triangle.
 

Constraints:

nums.length == 3
1 <= nums[i] <= 100
"""



def triangleType(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    if not len(nums) == 3:
        return "none"

    if (nums[0] + nums[1] <= nums[2]) or (nums[0] + nums[2] <= nums[1]) or (nums[1] + nums[2] <= nums[0]) :
        return "none"
    
    a = len(set(nums))
    if a == 1:
        return "equilateral"
    elif a == 2:
        return "isosceles"
    else:
        return "scalene"
    