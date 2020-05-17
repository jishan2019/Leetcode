# 1030. Matrix Cells in Distance Order
# Linked List


# reference form https://blog.csdn.net/fuxuemingzhu/article/details/100170598
class Solution:
	def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
		distance = []
		for r in range(R):
			for c in range(C):
				distance.append((abs(r0 - r) + abs(c0 - c), [r, c]))
		distance.sort()

		return [x for d, x in distance]


