# 215. Kth Largest Element in an Array
# Find the kth largest element in an unsorted array.
# Note that it is the kth largest element in the
# sorted order, not the kth distinct element.

# Example 1:
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
#
# Example 2:
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.

#1 using heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq as hq
        heap = nums[:k]
        hq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                hq.heapreplace(heap, num)
        return heap[0]


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]


#2 Quickselect

'''
kth largest element is equal to the (N-k)th smallest element.


'''