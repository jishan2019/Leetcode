# 206.Reverse Linked List
# Reverse a singly linked list.
#
# Example:
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
# Follow up:
# A linked list can be reversed either iteratively or recursively. Could you implement both?


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # create dummy, dummy.next = None
        # starting from node.val=1
        # dummy.next, head.next= head, dummy.next
        # dummy -> 1 -> NULL
        # iteration head = 2, dummy.next = 1
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next