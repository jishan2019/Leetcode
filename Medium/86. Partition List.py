# 86. Partition List
# Linked List
# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
	def partition(self, head: ListNode, x: int) -> ListNode:
		l = letter = ListNode(0)
		g = greater = ListNode(0)
		while head:
			if head.val < x:
				l.next = head
				l = head
			else:
				g.next = head
				g = head
			head = head.next

		g.next = None ##pay attention to this part!!

		l.next = greater.next

		return letter.next
