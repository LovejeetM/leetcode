"""
Problem 23

349. Intersection of Two Arrays
Easy
Topics
premium lock icon
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

"""


def intersection(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    inter= []
    nums1 = set(nums1)
    nums2 = set(nums2)
    for i in nums1:
        if i in nums2:
            inter.append(i)
    
    return inter

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1, nums2))