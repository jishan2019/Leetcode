# 1237. Find Positive Integer Solution for a Given Equation
# binary search

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


# reference from https://www.jianshu.com/p/ba2b966f35e2
class Solution:
	def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
		return filter(lambda x: customfunction.f(*x) == z, itertools.product(range(1, z + 1), repeat=2))


#