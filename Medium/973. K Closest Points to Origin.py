# 973. K Closest Points to Origin
# divided and conquer; sort

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
        return res[:K]