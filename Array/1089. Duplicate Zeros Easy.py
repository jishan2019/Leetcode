"""
1089. Duplicate Zeros Easy

Companies: Google
Tag: Array


Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining
elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place, do not return anything from your function.



Example 1:
Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:
Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:
1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""


""" Solution: """


## Two pass, O(1) space

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        possible_dups = 0
        length_ = len(arr) - 1

        # Find the number of zeros to be duplicated
        for left in range(length_ + 1):

            # Stop when left points beyond the last element in the original list
            # which would be part of the modified list
            if left > length_ - possible_dups:
                break

            # Count the zeros
            if arr[left] == 0:
                # Edge case: This zero can't be duplicated. We have no more space,
                # as left is pointing to the last element which could be included
                if left == length_ - possible_dups:
                    arr[length_] = 0 # For this zero we just copy it without duplication.
                    length_ -= 1
                    break
                possible_dups += 1

        # Start backwards from the last element which would be part of new list.
        last = length_ - possible_dups

        # Copy zero twice, and non zero once.
        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + possible_dups] = 0
                possible_dups -= 1
                arr[i + possible_dups] = 0
            else:
                arr[i + possible_dups] = arr[i]


# solution 2
#

"""
original arr:
[1, 0, 2, 0, 3, 0]
num of zeros so far:
[0, 1, 1, 2, 2, 3]
arr with duplicate 0s (Θ means a duplicate 0):
[1, Θ, 0, 2, Θ, 0, 3, Θ, 0]
arr after cutoff
[1, Θ, 0, 2, Θ, 0]

# Every number in the original array is shifted to the right by the number of zeros so far.
# Because of the cutoff, we are going to check if the new position of the number is inside the array.
if i + zeroes < n:
# This is checking if there is a Θ that should be included.
if arr[i] == 0:
  zeroes -= 1
  if i + zeroes < n:
     arr[i + zeroes] = 0
"""
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0:
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0