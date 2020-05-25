# 849. Maximize Distance to Closest Person
# array


# using groupby
class Solution:
	def maxDistToClosest(self, seats: List[int]) -> int:
		ans = 0
		groups = itertools.groupby(seats)
		for seat, group in groups:
			if not seat:
				ans = max(ans, (len(list(group)) + 1) // 2)  # convert group to list and then get the length
		return max(ans, seats.index(1), seats[::-1].index(1))  # pay attention to slice
