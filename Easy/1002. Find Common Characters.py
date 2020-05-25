# 1002. Find Common Characters
# array; hashtable

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        from functools import reduce
        return list(reduce(lambda x, y: x & y, map(Counter, A)).elements())