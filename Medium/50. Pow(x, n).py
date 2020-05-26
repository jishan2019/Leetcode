# 50. Pow(x, n)
# math

class Solution:
	def myPow(self, x: float, n: int) -> float:
		if n < 0:
			return 1 / self.pow_with_unsigned(x, -n)
		else:
			return self.pow_with_unsigned(x, n)

	def pow_with_unsigned(self, x, n):
		if n == 1:
			return x
		if n == 0:
			return 1

		res = self.pow_with_unsigned(x, n >> 1)
		res *= res

		if n & 1 == 1:
			res *= x

		return res