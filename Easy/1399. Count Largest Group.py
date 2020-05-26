# 1399. Count Largest Group
# array

class Solution:
    def countLargestGroup(self, n: int) -> int:
        import statistics
        return len(statistics.multimode(sum(map(int, str(d))) for d in range(1, n+1)))