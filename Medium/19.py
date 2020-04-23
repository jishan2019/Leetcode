# 19 Remove Nth Node From End of List
# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
# Note:
# Given n will always be valid.
# Follow up:
# Could you do this in one pass?


# using pointers to solve (slow pointer and fast pointer )
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        :type head: ListNode
        :type n: int
        """
        dummy = ListNode(0)
        dummy.next = head
        fast, slow, pre = dummy, dummy, dummy
        while n - 1:
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            pre = slow
            slow = slow.next
        pre.next = slow.next
        return dummy.next

