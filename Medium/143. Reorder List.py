# 143. Reorder List
# Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def reorderList(self, head: ListNode) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""
		if not head:
			return

		slow = fast = head
		while fast and fast.next:
			slow, fast = slow.next, fast.next.next

		tail, slow.next = slow.next, None

		def reverse(node):
			prev = None
			while node:
				node.next, prev, node = prev, node, node.next
			return prev

		tail = reverse(tail)
		h = head
		while h and tail:
			h.next, tail.next, tail, h = tail, h.next, tail.next, h.next