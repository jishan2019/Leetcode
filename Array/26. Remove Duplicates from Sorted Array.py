# 26. Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appear
# only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input
# array in-place with O(1) extra memory.



## using count
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        # consider the scenario--> the nums is not exist
        if not nums:
            return 0

        # start the count == 0;
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1

