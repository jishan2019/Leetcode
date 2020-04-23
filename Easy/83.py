# 83 Remove Duplicates from Sorted List
# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
# Input: 1->1->2
# Output: 1->2
#
# Example 2:
# Input: 1->1->2->3->3
# Output: 1->2->3


##1
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        dummy = head
        while current:
            runner = current.next
            while runner and current.val == runner.val:
                runner = runner.next
            current.next = runner
            current = runner
        return head


##2
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = head
        while pre:
            if pre.next and pre.next.val == pre.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return head