# 167. Two Sum II - Input array is sorted
# binary search; Array; two pointers


# Example:
#
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointers to solve
        left,right=0,len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left+1,right+1]
            elif numbers[left] + numbers[right] > target:
                right -=1
            else:
                left +=1