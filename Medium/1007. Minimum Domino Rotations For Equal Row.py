# 1007. Minimum Domino Rotations For Equal Row
# array; greedy


# try to find the min value then we can get the answer; we don't have to figure out the duplicates
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        ans = reduce(lambda x, y: x & y, map(set, zip(A, B)))
        if not ans:
            return -1
        else:
            a = ans.pop()
            return min(len(A)-A.count(a), len(B)-B.count(a))