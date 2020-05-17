# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# linked list


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        p = dummy = ListNode(0)
        dummy.next = head
        s = 0
        s_sum = [s]
        vals = {}
        while p:
            s += p.val
            s_sum.append(s)
            if s not in vals:
                vals[s] = p
            else:
                vals[s].next = p.next
                s_sum.pop() # here we remove the cur, and keep the last
                while s_sum[-1] != s:
                    vals.pop(s_sum.pop())
            p = p.next
        return dummy.next

# reference from https://darktiantian.github.io/LeetCode%E7%AE%97%E6%B3%95%E9%A2%98%E6%95%B4%E7%90%86%EF%BC%88%E9%93%BE%E8%A1%A8%E7%AF%87%EF%BC%89LinkedList/