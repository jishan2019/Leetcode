# 82. Remove Duplicates from Sorted List II
#
# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
# Return the linked list sorted as well.
#
# Example 1:
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
# Example 2:
# Input: 1->1->1->2->3
# Output: 2->3

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        root = ListNode(0)
        root.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        counter = collections.Counter(val_list)
        head = root
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return root.next
