#904.Fruit Into Baskets
# In a row of trees, the i-th tree produces fruit with type tree[i].
#
# You start at any tree of your choice, then repeatedly perform the following steps:
#
# Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
# Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.
#
# You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.
#
# What is the total amount of fruit you can collect with this procedure?

#two pointers


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        from collections import Counter
        basket = Counter()
        l, res = 0, 0
        for r in range(len(tree)):
            basket[tree[r]] += 1
            while len(basket) > 2:
                basket[tree[l]] -= 1
                if basket[tree[l]] == 0:
                    basket.pop(tree[l])
                l += 1
            res = max(res, r-l+1)
        return res


#solution from leetcode
class Solution(object):
    def totalFruit(self, tree):
        blocks = [(k, len(list(v)))
                  for k, v in itertools.groupby(tree)]

        ans = i = 0
        while i < len(blocks):
            # We'll start our scan at block[i].
            # types : the different values of tree[i] seen
            # weight : the total number of trees represented
            #          by blocks under consideration
            types, weight = set(), 0

            # For each block from i and going forward,
            for j in xrange(i, len(blocks)):
                # Add each block to consideration
                types.add(blocks[j][0])
                weight += blocks[j][1]

                # If we have 3 types, this is not a legal subarray
                if len(types) >= 3:
                    i = j-1
                    break

                ans = max(ans, weight)

            # If we go to the last block, then stop
            else:
                break

        return ans