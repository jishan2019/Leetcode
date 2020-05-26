# 1394. Find Lucky Integer in an Array
# array


# wrong answer
# class Solution:
#     def findLucky(self, arr: List[int]) -> int:
#         from collections import Counter
#         c = Counter(arr)
#         for d, f in c.most_common():
#             if d == f:
#                 return d
#             return -1