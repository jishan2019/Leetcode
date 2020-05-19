# 724. Find Pivot Index
# array


# using pointers
def pivotIndex(self, nums):
    left, right, i = 0, sum(nums), 0
    while i < len(nums):
        left += nums[i-1] if i > 0 else 0
        right -= nums[i]
        if left == right:
            return i
        i += 1
    return -1