# 1375. Bulb Switcher III
# array



# use enumerate to solve
class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        cur_max = ans = 0
        for i, b in enumerate(light, 1):
            cur_max = max(cur_max, b)
            if cur_max == i:
                ans += 1
        return ans