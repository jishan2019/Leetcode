# 445. Add Two Numbers II
#linked list

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the lists is not allowed.


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1 = v2 = 0
        while l1:
            v1 = v1*10 + l1.val
            l1 = l1.next
        while l2:
            v2 = v2*10 + l2.val
            l2 = l2.next
        val = v1 + v2
        tail, head = None, None
        while val > 0:
            head = ListNode(val % 10)
            head.next = tail
            tail = head
            val //= 10
        return head if head else ListNode(0)