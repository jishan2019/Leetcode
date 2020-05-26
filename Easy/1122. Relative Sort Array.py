# 1122. Relative Sort Array
# array; sort


# can use addition/ multiplication to solve
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {d: i for i, d in enumerate(arr2)}
        return sorted(arr1, key=lambda x: index.get(x, 1000+x))