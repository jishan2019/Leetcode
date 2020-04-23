# 88. Merge Sorted Array
# 04/20/2020
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]

# https://leetcode.com/problems/merge-sorted-array/description/


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m - 1 + n] = nums2[n - 1]
                n = n - 1
            else:
                nums1[m - 1 + n], nums1[m - 1] = nums1[m - 1], nums1[m - 1 + n]  # swap
                m = m - 1
        if m == 0 and n > 0:
            nums1[:n] = nums2[:n]


##2
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums = [n1 for i, n1 in enumerate(nums1) if i < m] + [n2 for i, n2 in enumerate(nums2) if i < n]
        nums.sort()
        for i, num in enumerate(nums):
            nums1[i] = num

