# 605. Can Place Flowers
# array

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        plots = [0] + flowerbed + [0]
        p = 1
        while p <= len(flowerbed) and n > 0:
            if plots[p] == 0 and plots[p-1] == 0 and plots[p+1] == 0:
                plots[p] = 1
                n -= 1
            p += 1
        return n == 0