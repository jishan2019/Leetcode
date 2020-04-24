# 860. Lemonade Change
# At a lemonade stand, each lemonade costs $5.
# Customers are standing in a queue to buy from you, and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  You must provide the correct change to each customer, so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# Example 1:
#
# Input: [5,5,5,10,20]
# Output: true
# Explanation:
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2:
#
# Input: [5,5,10]
# Output: true

# Example 3:
#
# Input: [10,10]
# Output: false

#using defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c = collections.defaultdict(int)
        for bill in bills:
            if bill == 10:
                c[5] -= 1
            elif bill == 20:
                if c[10] >= 1:
                    c[10] -= 1
                    c[5] -= 1
                else:
                    c[5] -= 3
            if c[5] < 0:
                return False
            c[bill] += 1
        return True


#solution from leetcode
class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True


# 3

class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        changes = {5:0, 10:0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False
                else:
                    changes[10] += 1
                    changes[5] -= 1
            elif bill == 20:
                if changes[10] != 0:
                    if changes[5] == 0:
                        return False
                    else:
                        changes[5] -= 1
                        changes[10] -= 1
                else:
                    if changes[5] < 3:
                        return False
                    else:
                        changes[5] -= 3
        return True
