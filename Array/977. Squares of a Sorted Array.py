"""
977. Squares of a Sorted Array

Companies: Facebook 17 Uber 6 Amazon5 Google 2
Related Topics: Array; Two Pointers

===============================================
Given an integer array nums sorted in non-decreasing order, return an array of the squares of
each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Follow up: Squaring each element and sorting the new array is very trivial,
could you find an O(n) solution using a different approach?
"""

class Solution1:
    def sortedSquares(self, nums):
		return sorted(x*x for x in nums)

"""
Sort:
Complexity Analysis

Time Complexity: O(N \log N)O(NlogN), where NN is the length of A.

Space complexity : \mathcal{O}(N)O(N) or \mathcal{O}(\log{N})O(logN)

The space complexity of the sorting algorithm depends on the implementation of each program language.

For instance, the list.sort() function in Python is implemented with the Timsort algorithm whose space 
complexity is \mathcal{O}(N)O(N).

In Java, the Arrays.sort() is implemented as a variant of quicksort algorithm whose space complexity is 
\mathcal{O}(\log{N})O(logN)."""

class Solution(object):
	def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans

"""
Two Pointers:
Since the array A is sorted, loosely speaking it has some negative elements with squares in decreasing
order, then some non-negative elements with squares in increasing order.

For example, with [-3, -2, -1, 4, 5, 6], we have the negative part [-3, -2, -1] with squares [9, 4, 1],
and the positive part [4, 5, 6] with squares [16, 25, 36]. Our strategy is to iterate over the negative
part in reverse, and the positive part in the forward direction.

Algorithm

We can use two pointers to read the positive and negative parts of the array - one pointer j in the
positive direction, and another i in the negative direction.

Now that we are reading two increasing arrays (the squares of the elements), we can merge these arrays
together using a two-pointer technique.

"""

