"""
Problem 33:

350. Intersection of Two Arrays II
Easy
Topics
premium lock icon
Companies
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    
    inter = []
    nums1.sort()
    nums2.sort()
    

    used = set()
    used1 = set()
    for i, ch in enumerate(nums1):
        for j, char in enumerate(nums2):
            if j not in used1 and i not in used and ch == char:
                used1.add(j)
                used.add(i)

    # print(used)
    inter = [nums1[i] for i in used]
    return inter

    # inter = []
    # nums1.sort()
    # nums2.sort()
    # used = {}
    
    # for ch in nums1:
    #     for char in nums2:
    #         if ch not in used and ch == char:
    #             used[ch] = 1
    #         if ch in used and ch == char:
    #             used[ch] += 1
    

    # print(used.items())
    # for c in used:
    #     for i in range(0, used[c]-1):
    #         inter.append(c)
    # return inter

nums1 = [1,2,2,1]
nums2 = [2]
print(intersect(nums1, nums2))
    