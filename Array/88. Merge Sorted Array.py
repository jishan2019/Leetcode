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

#

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Write the elements of num2 into the end of nums1.
        for i in range(n):
            nums1[i + m] = nums2[i]

        # Sort nums1 list in-place.
        nums1.sort()


# three pointers
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Make a copy of the first m elements of nums1.
        nums1_copy = nums1[:m]

        # Read pointers for nums1Copy and nums2 respectively.
        p1 = 0
        p2 = 0

        # Compare elements from nums1Copy and nums2 and write the smallest to nums1.
        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries
            # of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
