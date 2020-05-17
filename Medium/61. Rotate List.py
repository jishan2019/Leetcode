# 61. Rotate List
# Linked List

# Given a linked list, rotate the list to the right by k places, where k is non-negative.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def rotateRight(self, head: ListNode, k: int) -> ListNode:
		n, cur, prev = 0, head, None
		while cur:
			n += 1
			prev, cur = cur, cur.next

		if n == 0 or k % n == 0:
			return head

		k = k % n

		tail = head

		for _ in range(n - k - 1):
			tail = tail.next

		ans, tail.next, prev.next = tail.next, None, head

		return ans