# 1351. Count Negative Numbers in a Sorted Matrix
# binary search; array

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        # reference: https://medium.com/@donic0211/leetcode-1351-count-negative-numbers-in-a-sorted-matrix-cb60cb62ecdd
        # traverse the list and return the count
        count=0
        for m in grid:
            for n in m:
                if n < 0:
                    count+=1
        return count