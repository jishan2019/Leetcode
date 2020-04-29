# 23. Merge k Sorted Lists
# linked list; Divided and conquer; heap

# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        q = PriorityQueue()
        for idx, l in enumerate(lists):
            if l:
                q.put((l.val, idx, l))
        h = head = ListNode(0)
        while not q.empty():
            val, idx, node = q.get()
            h.next = node
            h, node = h.next, node.next
            if node:
                q.put((node.val, idx, node))
        return head.next
