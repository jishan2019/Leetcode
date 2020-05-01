# 148. Sort List


# Linked List; sort

# Sort a linked list in O(n log n) time using constant space complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def sortList(self, head: ListNode) -> ListNode:

		def merge_list(l1, l2):
			l = h = ListNode(0)
			while l1 and l2:
				if l1.val <= l2.val:
					l.next, l1 = l1, l1.next
				else:
					l.next, l2 = l2, l2.next
				l = l.next
			l.next = l1 or l2
			return h.next

		def merge_sort(h):
			if not h or not h.next:
				return h
			slow = fast = h
			prev = None
			while fast and fast.next:
				pre, slow, fast = slow, slow.next, fast.next.next
			pre.next = None
			left = merge_sort(h)
			right = merge_sort(slow)
			return merge_list(left, right)

		return merge_sort(head)