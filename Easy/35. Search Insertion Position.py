# 35. Search Insertion Position
# #
# # Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array.
# # Example 1:
# # Input: [1,3,5,6], 5
# # Output: 2
# # Example 2:
# # Input: [1,3,5,6], 2
# # Output: 1
# # Example 3:
# # Input: [1,3,5,6], 7
# # Output: 4
# # Example 4:
# # Input: [1,3,5,6], 0
# # Output: 0
# #
# # From <https://leetcode.com/problems/search-insert-position/>

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # consider two scenarios: 1 the target is bigger then the element in nums, the position will the last index
        if target > nums[len(nums) - 1]:
            return len(nums)
        # 2 the target is less than one of the element in nums, comparing these two and return the index of the element in num
        for i in range(len(nums)):
            if nums[i] >= target:
                return i


